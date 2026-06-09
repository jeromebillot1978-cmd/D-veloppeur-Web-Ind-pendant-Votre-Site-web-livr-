// app/api/generate-pub/route.js
// Route API sécurisée — la clé Groq reste côté serveur (jamais exposée)

const BUSINESS_LABELS = {
  restaurant: "Restaurant / Café",
  coiffeur:   "Coiffeur / Barbier",
  artisan:    "Artisan / BTP",
  coach:      "Coach / Consultant",
  boutique:   "Boutique / Commerce",
};

const OBJECTIF_LABELS = {
  leads:    "Générer des Leads",
  whatsapp: "Messages WhatsApp",
  appels:   "Appels téléphoniques",
  visites:  "Visites du site web",
};

export async function POST(request) {
  try {
    const { businessType, nom, ville, offre, objectif } = await request.json();

    // Validation basique
    if (!nom?.trim() || !ville?.trim() || !offre?.trim()) {
      return Response.json({ error: "Champs manquants" }, { status: 400 });
    }

    const businessLabel = BUSINESS_LABELS[businessType] || businessType;
    const objectifLabel = OBJECTIF_LABELS[objectif]     || objectif;

    const userPrompt = `Génère exactement 3 variantes de publicités Meta Ads pour :
- Type : ${businessLabel}
- Nom : ${nom}
- Ville : ${ville}
- Offre : ${offre}
- Objectif : ${objectifLabel}

Contraintes STRICTES par variante :
- titre : max 40 caractères
- texte : max 125 caractères avec 1-2 émojis et CTA clair
- description : max 30 caractères
- prompt_image : description anglaise détaillée pour DALL-E 1080x1080, photo pro publicitaire adaptée au métier et à ${ville}, sans texte dans l'image
- ciblage_age : tranche d'âge optimale (ex: "25-45 ans")
- interets : exactement 3 centres d'intérêt Meta précis
- rayon_km : rayon optimal en km (entier)

Angles : variante 1 = émotionnel, variante 2 = rationnel/offre, variante 3 = urgence.

JSON uniquement :
{"pubs":[{"angle":"Émotionnel","titre":"...","texte":"...","description":"...","prompt_image":"...","ciblage_age":"...","interets":["...","...","..."],"rayon_km":10}]}`;

    const groqRes = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${process.env.GROQ_API_KEY}`,  // ← côté serveur, sécurisé
      },
      body: JSON.stringify({
        model: "llama-3.3-70b-versatile",
        max_tokens: 1500,
        temperature: 0.7,
        response_format: { type: "json_object" },
        messages: [
          {
            role: "system",
            content: "Tu es copywriter expert Meta Ads pour TPE/PME françaises. Réponds UNIQUEMENT en JSON valide, sans texte ni markdown.",
          },
          { role: "user", content: userPrompt },
        ],
      }),
    });

    const groqData = await groqRes.json();

    if (groqData.error) {
      console.error("Groq error:", groqData.error);
      return Response.json({ error: groqData.error.message }, { status: 500 });
    }

    const raw    = groqData.choices?.[0]?.message?.content || "";
    const clean  = raw.replace(/```json|```/g, "").trim();
    const parsed = JSON.parse(clean);

    return Response.json(parsed);

  } catch (err) {
    console.error("generate-pub error:", err);
    return Response.json({ error: "Erreur interne, réessaie." }, { status: 500 });
  }
}
