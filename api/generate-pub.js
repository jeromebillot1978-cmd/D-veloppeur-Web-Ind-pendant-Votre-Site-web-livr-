export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { activite, ton, format, promo, infos } = req.body;

  if (!activite) {
    return res.status(400).json({ error: 'Activité manquante' });
  }

  const prompt = `Tu es un expert en copywriting publicitaire français.
Rédige une publicité ${format} pour un(e) ${activite}.
Ton souhaité : ${ton}.${promo ? `\nOffre à mettre en avant : ${promo}.` : ''}${infos ? `\nInfos complémentaires : ${infos}.` : ''}
Réponds uniquement avec le texte publicitaire, sans explication, sans balises markdown.`;

  try {
    const response = await fetch('https://api.groq.com/openai/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${process.env.GROQ_API_KEY}`
      },
      body: JSON.stringify({
        model: 'llama-3.1-8b-instant',
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 500,
        temperature: 0.85
      })
    });

    if (!response.ok) {
      const err = await response.json().catch(() => ({}));
      return res.status(response.status).json({ error: err?.error?.message || 'Erreur Groq' });
    }

    const data = await response.json();
    const texte = data.choices?.[0]?.message?.content?.trim() || 'Aucun résultat.';
    return res.status(200).json({ texte });

  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
}
