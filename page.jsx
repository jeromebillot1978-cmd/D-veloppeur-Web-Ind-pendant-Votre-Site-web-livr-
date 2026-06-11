"use client";

import { useState } from "react";
import Head from "next/head";

const BUSINESS_TYPES = [
  { value: "restaurant", label: "🍽 Restaurant / Café" },
  { value: "coiffeur",   label: "✂️ Coiffeur / Barbier" },
  { value: "artisan",    label: "🔧 Artisan / BTP" },
  { value: "coach",      label: "🎯 Coach / Consultant" },
  { value: "boutique",   label: "🛍 Boutique / Commerce" },
];

const OBJECTIVES = [
  { value: "leads",     label: "📋 Générer des Leads" },
  { value: "whatsapp",  label: "💬 Messages WhatsApp" },
  { value: "appels",    label: "📞 Appels téléphoniques" },
  { value: "visites",   label: "🌐 Visites du site web" },
];

export default function GenerateurPub() {
  const [form, setForm] = useState({
    businessType: "restaurant",
    nom: "",
    ville: "",
    offre: "",
    objectif: "leads",
  });
  const [results, setResults]   = useState(null);
  const [loading, setLoading]   = useState(false);
  const [error, setError]       = useState("");
  const [copied, setCopied]     = useState({});

  const handleChange = (e) =>
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));

  /* ── Appel vers /api/generate-pub (route sécurisée) ── */
  async function generate() {
    if (!form.nom.trim() || !form.ville.trim() || !form.offre.trim()) {
      setError("Remplis tous les champs avant de générer.");
      return;
    }
    setError("");
    setResults(null);
    setLoading(true);

    try {
      const res = await fetch("/api/generate-pub", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "Erreur serveur");
      setResults(data.pubs);
    } catch (e) {
      setError(e.message || "Erreur lors de la génération. Réessaie.");
    } finally {
      setLoading(false);
    }
  }

  /* ── Copier tout le bloc ── */
  function copyBlock(pub, idx) {
    const txt = `✦ PUB META — ${pub.angle.toUpperCase()}

📌 TITRE (${pub.titre.length}/40) :
${pub.titre}

📝 TEXTE PRINCIPAL (${pub.texte.length}/125) :
${pub.texte}

📄 DESCRIPTION (${pub.description.length}/30) :
${pub.description}

🖼 PROMPT IMAGE DALL-E (1080×1080) :
${pub.prompt_image}

🎯 CIBLAGE META :
• Âge : ${pub.ciblage_age}
• Centres d'intérêt : ${pub.interets.join(", ")}
• Rayon : ${pub.rayon_km} km autour de ${form.ville}`;

    navigator.clipboard.writeText(txt).then(() => {
      setCopied((p) => ({ ...p, [idx]: true }));
      setTimeout(() => setCopied((p) => ({ ...p, [idx]: false })), 2200);
    });
  }

  /* ── Compteur de caractères coloré ── */
  function cc(str, max) {
    const n = str?.length || 0;
    const c = n > max ? "#ff4757" : n > max * 0.85 ? "#f4a31a" : "#22d678";
    return <span style={{ fontSize: "0.7rem", color: c, fontFamily: "monospace" }}>{n}/{max}</span>;
  }

  /* ════════════════════════════════════════════════════════ RENDER */
  return (
    <>
      <Head>
        <title>Générateur de Pubs Meta IA — Jercat Développeur Web</title>
        <meta name="description" content="Génère 3 publicités Facebook/Instagram optimisées en quelques secondes grâce à l'IA Llama 3. Outil gratuit par Jercat." />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,800;1,700;1,800&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
      </Head>

      <style>{CSS}</style>

      {/* NAV */}
      <nav className="nav">
        <a href="/" className="nav-logo">Jer<em>cat</em></a>
        <span className="nav-badge">IA · Llama 3</span>
        <a href="/" className="nav-back">← Retour au site</a>
      </nav>

      {/* HERO */}
      <section className="hero">
        <div className="hero-eyebrow"><span className="spark">✦</span>Outil gratuit — Développeur Web IA</div>
        <h1>Générateur de pubs<br /><em>Meta</em> par IA</h1>
        <p className="hero-sub">Crée 3 publicités Facebook & Instagram optimisées en quelques secondes. Titres, textes, ciblage et prompts image inclus.</p>
        <div className="hero-pills">
          <span className="pill"><span className="dot" />Gratuit &amp; sans inscription</span>
          <span className="pill"><span className="dot" />Facebook &amp; Instagram Ads</span>
          <span className="pill"><span className="dot" />Limites Meta respectées</span>
          <span className="pill"><span className="dot" />Propulsé par Llama 3</span>
        </div>
      </section>

      {/* FORM */}
      <div className="form-section">
        <div className="card">
          <div className="card-title">✦ Ton business</div>
          <div className="form-grid">
            <div className="field">
              <label>Type de business</label>
              <select name="businessType" value={form.businessType} onChange={handleChange}>
                {BUSINESS_TYPES.map((b) => <option key={b.value} value={b.value}>{b.label}</option>)}
              </select>
            </div>
            <div className="field">
              <label>Objectif pub</label>
              <select name="objectif" value={form.objectif} onChange={handleChange}>
                {OBJECTIVES.map((o) => <option key={o.value} value={o.value}>{o.label}</option>)}
              </select>
            </div>
            <div className="field">
              <label>Nom du business *</label>
              <input type="text" name="nom" value={form.nom} onChange={handleChange} placeholder="Ex : Chez Mario, Studio Zara…" maxLength={60} />
            </div>
            <div className="field">
              <label>Ville *</label>
              <input type="text" name="ville" value={form.ville} onChange={handleChange} placeholder="Ex : Paris, Lyon, Bordeaux…" maxLength={50} />
            </div>
            <div className="field full">
              <label>Offre / accroche principale *</label>
              <input type="text" name="offre" value={form.offre} onChange={handleChange} placeholder="Ex : Menu burger + frites offert ce week-end" maxLength={120} />
            </div>
          </div>
        </div>

        {error && <div className="error-msg">⚠ {error}</div>}

        <button className="btn-generate" onClick={generate} disabled={loading}>
          {loading
            ? <><Spinner />Génération en cours…</>
            : <>✦ Générer 3 pubs Meta</>}
        </button>

        {loading && (
          <div className="loader-wrap">
            <div className="loader-ring" />
            <div className="loader-text">Llama 3 rédige tes publicités…</div>
          </div>
        )}

        {/* RESULTS */}
        {results && (
          <div style={{ marginTop: 36 }}>
            <div className="results-header">
              <div className="results-title">3 pubs <em>prêtes à diffuser</em></div>
              <span style={{ fontSize: "0.75rem", color: "var(--muted)", fontFamily: "JetBrains Mono, monospace" }}>
                pour {form.nom} · {form.ville}
              </span>
            </div>

            {results.map((pub, idx) => (
              <div className="pub-card" key={idx}>
                <div className="pub-card-header">
                  <span className={`pub-angle-badge angle-${idx}`}>
                    {["❤ Émotionnel", "📊 Rationnel", "⚡ Urgence"][idx]}
                  </span>
                  <span style={{ fontSize: "0.75rem", color: "var(--muted)", marginLeft: "auto" }}>
                    Variante {idx + 1} / 3
                  </span>
                </div>

                <div className="pub-card-body">
                  <Field label={<>📌 Titre {cc(pub.titre, 40)}</>} bold>{pub.titre}</Field>
                  <Field label={<>📝 Texte principal {cc(pub.texte, 125)}</>}>{pub.texte}</Field>
                  <Field label={<>📄 Description {cc(pub.description, 30)}</>}>{pub.description}</Field>

                  <hr className="divider" />

                  <Field label="🖼 Prompt image DALL-E · 1080×1080" mono>{pub.prompt_image}</Field>

                  <hr className="divider" />

                  {/* Ciblage */}
                  <div className="pub-field">
                    <div className="pub-field-label">🎯 Ciblage Meta Ads</div>
                    <div className="targeting-grid">
                      <div className="targeting-item">
                        <div className="targeting-item-label">Âge</div>
                        <div className="targeting-item-value">{pub.ciblage_age}</div>
                      </div>
                      <div className="targeting-item">
                        <div className="targeting-item-label">Rayon</div>
                        <div className="targeting-item-value">{pub.rayon_km} km — {form.ville}</div>
                      </div>
                      <div className="targeting-item" style={{ gridColumn: "1 / -1" }}>
                        <div className="targeting-item-label" style={{ marginBottom: 6 }}>Centres d'intérêt</div>
                        <div className="interets-list">
                          {pub.interets.map((t, i) => <span key={i} className="interet-tag">{t}</span>)}
                        </div>
                      </div>
                    </div>
                  </div>

                  <button className={`btn-copy${copied[idx] ? " ok" : ""}`} onClick={() => copyBlock(pub, idx)}>
                    {copied[idx] ? "✓ Copié !" : "📋 Copier tout le bloc"}
                  </button>
                </div>
              </div>
            ))}

            {/* CTA */}
            <div className="card" style={{ textAlign: "center", marginTop: 8, borderColor: "rgba(201,168,76,0.15)" }}>
              <p style={{ fontSize: "0.9rem", color: "var(--muted)", marginBottom: 14, lineHeight: 1.7 }}>
                Tu veux un site web qui convertit autant que tes pubs ?
              </p>
              <a href="/#contact" className="btn-cta">✦ Demander un devis gratuit</a>
            </div>
          </div>
        )}
      </div>

      {/* FOOTER */}
      <footer className="footer">
        <div className="footer-left">
          <div className="footer-logo">Jer<em>cat</em></div>
          <div style={{ marginTop: 4 }}>Développeur Web Freelance — <a href="/">jercat.vercel.app</a></div>
        </div>
        <div className="footer-right">
          Propulsé par Llama 3 via Groq<br />
          <a href="/" style={{ color: "var(--muted)", textDecoration: "none", fontSize: "0.72rem" }}>← Retour à l'accueil</a>
        </div>
      </footer>
    </>
  );
}

/* ── Sous-composants ── */
function Field({ label, children, bold, mono }) {
  return (
    <div className="pub-field">
      <div className="pub-field-label">{label}</div>
      <div className={`pub-field-value${mono ? " prompt" : ""}`} style={bold ? { fontWeight: 600 } : {}}>
        {children}
      </div>
    </div>
  );
}

function Spinner() {
  return <span style={{ width: 18, height: 18, border: "2px solid rgba(0,0,0,0.2)", borderTopColor: "#0a0a08", borderRadius: "50%", display: "inline-block", animation: "spin 0.7s linear infinite" }} />;
}

/* ════════════════════════════════════════════════════════ CSS */
const CSS = `
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  :root {
    --bg: #0a0a08; --bg2: #111110; --bg3: #181816; --bg4: #1e1e1b;
    --border: rgba(255,255,255,0.07); --border2: rgba(255,255,255,0.12);
    --text: #e8e6e0; --muted: #6b6860;
    --gold: #c9a84c; --gold2: #f4cc7a;
    --accent: #1877f2; --green: #22d678; --red: #ff4757; --r: 10px;
  }
  body { background: var(--bg); color: var(--text); font-family: 'Inter', sans-serif; font-size: 15px; line-height: 1.6; -webkit-font-smoothing: antialiased; }

  .nav { position: sticky; top: 0; z-index: 100; background: rgba(10,10,8,0.93); backdrop-filter: blur(14px); border-bottom: 1px solid var(--border); padding: 0 clamp(16px,5vw,60px); display: flex; align-items: center; gap: 14px; height: 62px; }
  .nav-logo { font-family: 'Playfair Display', serif; font-weight: 800; font-size: 1.25rem; color: var(--text); text-decoration: none; letter-spacing: -0.5px; }
  .nav-logo em { font-style: italic; color: var(--gold); }
  .nav-badge { padding: 2px 9px; background: rgba(201,168,76,0.1); border: 1px solid rgba(201,168,76,0.25); border-radius: 20px; font-size: 0.65rem; letter-spacing: 1.5px; color: var(--gold); text-transform: uppercase; font-family: 'JetBrains Mono', monospace; }
  .nav-back { margin-left: auto; font-size: 0.8rem; color: var(--muted); text-decoration: none; transition: color 0.2s; }
  .nav-back:hover { color: var(--text); }

  .hero { text-align: center; padding: clamp(48px,8vw,100px) clamp(16px,5vw,60px) clamp(36px,5vw,64px); position: relative; overflow: hidden; }
  .hero::before { content: ''; position: absolute; top: -120px; left: 50%; transform: translateX(-50%); width: 600px; height: 400px; background: radial-gradient(ellipse, rgba(24,119,242,0.07) 0%, transparent 70%); pointer-events: none; }
  .hero-eyebrow { display: inline-flex; align-items: center; gap: 8px; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; letter-spacing: 2.5px; text-transform: uppercase; color: var(--gold); margin-bottom: 22px; }
  .spark { color: var(--gold2); }
  .hero h1 { font-family: 'Playfair Display', serif; font-weight: 800; font-size: clamp(2rem,5vw,3.4rem); line-height: 1.15; letter-spacing: -1px; margin-bottom: 18px; }
  .hero h1 em { font-style: italic; color: var(--gold2); }
  .hero-sub { font-size: clamp(0.9rem,2vw,1.05rem); color: var(--muted); max-width: 520px; margin: 0 auto 36px; font-weight: 300; line-height: 1.7; }
  .hero-pills { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }
  .pill { padding: 5px 14px; border: 1px solid var(--border2); border-radius: 20px; font-size: 0.75rem; color: var(--muted); display: flex; align-items: center; gap: 6px; }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: var(--green); display: inline-block; }

  .form-section { max-width: 780px; margin: 0 auto; padding: 0 clamp(16px,4vw,32px) 80px; }
  .card { background: var(--bg2); border: 1px solid var(--border); border-radius: var(--r); padding: clamp(20px,4vw,36px); margin-bottom: 20px; }
  .card-title { font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700; color: var(--gold); margin-bottom: 22px; }
  .form-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
  @media (max-width: 560px) { .form-grid { grid-template-columns: 1fr; } }
  .field { display: flex; flex-direction: column; gap: 7px; }
  .field.full { grid-column: 1 / -1; }
  label { font-size: 0.72rem; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); font-family: 'JetBrains Mono', monospace; }
  input, select { background: var(--bg3); border: 1px solid var(--border); border-radius: 8px; padding: 11px 14px; font-size: 0.88rem; font-family: 'Inter', sans-serif; color: var(--text); outline: none; width: 100%; transition: border-color 0.2s, box-shadow 0.2s; -webkit-appearance: none; }
  input:focus, select:focus { border-color: rgba(201,168,76,0.4); box-shadow: 0 0 0 3px rgba(201,168,76,0.06); }
  input::placeholder { color: var(--muted); }
  select option { background: #181816; }

  .btn-generate { width: 100%; margin-top: 6px; padding: 15px 24px; background: linear-gradient(135deg, #c9a84c 0%, #f4cc7a 50%, #c9a84c 100%); background-size: 200% auto; border: none; border-radius: 8px; font-family: 'Playfair Display', serif; font-size: 1.05rem; font-weight: 700; color: #0a0a08; cursor: pointer; transition: background-position 0.4s, transform 0.15s, box-shadow 0.2s; display: flex; align-items: center; justify-content: center; gap: 10px; }
  .btn-generate:hover:not(:disabled) { background-position: right center; transform: translateY(-1px); box-shadow: 0 6px 24px rgba(201,168,76,0.25); }
  .btn-generate:disabled { opacity: 0.6; cursor: not-allowed; }

  .loader-wrap { display: flex; flex-direction: column; align-items: center; gap: 16px; padding: 52px 20px; }
  .loader-ring { width: 40px; height: 40px; border: 3px solid var(--border2); border-top-color: var(--gold); border-radius: 50%; animation: spin 0.75s linear infinite; }
  @keyframes spin { to { transform: rotate(360deg); } }
  .loader-text { font-size: 0.82rem; color: var(--muted); font-family: 'JetBrains Mono', monospace; animation: blink 1.4s ease-in-out infinite; }
  @keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.4} }

  .error-msg { padding: 12px 16px; background: rgba(255,71,87,0.08); border: 1px solid rgba(255,71,87,0.25); border-radius: 8px; color: var(--red); font-size: 0.82rem; margin-top: 12px; }

  .results-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; }
  .results-title { font-family: 'Playfair Display', serif; font-size: 1.4rem; font-weight: 800; letter-spacing: -0.5px; }
  .results-title em { font-style: italic; color: var(--gold2); }

  .pub-card { background: var(--bg2); border: 1px solid var(--border); border-radius: var(--r); overflow: hidden; margin-bottom: 16px; animation: fadeUp 0.4s ease both; }
  .pub-card:nth-child(2) { animation-delay: 0.08s; }
  .pub-card:nth-child(3) { animation-delay: 0.16s; }
  @keyframes fadeUp { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }

  .pub-card-header { padding: 14px 20px; background: var(--bg3); border-bottom: 1px solid var(--border); display: flex; align-items: center; gap: 10px; }
  .pub-angle-badge { padding: 3px 11px; border-radius: 20px; font-size: 0.68rem; letter-spacing: 1px; font-family: 'JetBrains Mono', monospace; font-weight: 500; }
  .angle-0 { background: rgba(201,168,76,0.12); color: var(--gold); border: 1px solid rgba(201,168,76,0.2); }
  .angle-1 { background: rgba(24,119,242,0.12); color: #5ba3f5; border: 1px solid rgba(24,119,242,0.2); }
  .angle-2 { background: rgba(34,214,120,0.1); color: var(--green); border: 1px solid rgba(34,214,120,0.2); }

  .pub-card-body { padding: 20px; display: flex; flex-direction: column; gap: 14px; }
  .pub-field { display: flex; flex-direction: column; gap: 5px; }
  .pub-field-label { font-size: 0.65rem; letter-spacing: 2px; text-transform: uppercase; color: var(--muted); font-family: 'JetBrains Mono', monospace; display: flex; align-items: center; gap: 8px; }
  .pub-field-value { font-size: 0.9rem; line-height: 1.6; background: var(--bg3); border: 1px solid var(--border); border-radius: 7px; padding: 10px 14px; color: var(--text); }
  .pub-field-value.prompt { font-family: 'JetBrains Mono', monospace; font-size: 0.76rem; color: var(--muted); line-height: 1.7; }

  .targeting-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
  @media (max-width: 480px) { .targeting-grid { grid-template-columns: 1fr; } }
  .targeting-item { background: var(--bg3); border: 1px solid var(--border); border-radius: 7px; padding: 10px 13px; display: flex; flex-direction: column; gap: 4px; }
  .targeting-item-label { font-size: 0.62rem; letter-spacing: 1.5px; text-transform: uppercase; color: var(--muted); font-family: 'JetBrains Mono', monospace; }
  .targeting-item-value { font-size: 0.84rem; color: var(--text); }
  .interets-list { display: flex; flex-wrap: wrap; gap: 6px; }
  .interet-tag { padding: 3px 10px; background: rgba(201,168,76,0.08); border: 1px solid rgba(201,168,76,0.18); border-radius: 20px; font-size: 0.75rem; color: var(--gold); }

  .divider { border: none; border-top: 1px solid var(--border); }

  .btn-copy { align-self: flex-start; padding: 9px 18px; background: transparent; border: 1px solid var(--border2); border-radius: 7px; font-size: 0.78rem; color: var(--text); font-family: 'Inter', sans-serif; cursor: pointer; transition: all 0.18s; display: flex; align-items: center; gap: 7px; }
  .btn-copy:hover { background: var(--bg4); border-color: rgba(201,168,76,0.3); }
  .btn-copy.ok { border-color: rgba(34,214,120,0.4); color: var(--green); }

  .btn-cta { display: inline-flex; align-items: center; gap: 8px; padding: 11px 24px; background: linear-gradient(135deg, #c9a84c, #f4cc7a); border-radius: 8px; color: #0a0a08; font-family: 'Playfair Display', serif; font-weight: 700; font-size: 0.95rem; text-decoration: none; transition: opacity 0.2s; }
  .btn-cta:hover { opacity: 0.88; }

  .footer { border-top: 1px solid var(--border); padding: 32px clamp(16px,5vw,60px); display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 16px; }
  .footer-left { font-size: 0.78rem; color: var(--muted); }
  .footer-left a { color: var(--gold); text-decoration: none; }
  .footer-logo { font-family: 'Playfair Display', serif; font-weight: 800; font-size: 1rem; }
  .footer-logo em { font-style: italic; color: var(--gold); }
  .footer-right { font-size: 0.75rem; color: var(--muted); font-family: 'JetBrains Mono', monospace; text-align: right; }
`;
