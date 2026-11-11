# -*- coding: utf-8 -*-
"""
Contenu des pages nationales de dev.jercat.fr (services, études de cas, blog).
Modifier les textes ici, puis lancer :  python3 gen/build.py
Le HTML de chaque section accepte des balises simples (<p>, <ul>, <li>, <strong>, <a>).
"""

TEL = "06 31 04 03 64"
TEL_LINK = "tel:+33631040364"

# --------------------------------------------------------------------------------------
# PAGES DE SERVICES
# --------------------------------------------------------------------------------------
SERVICES = [
  {
    "slug": "creation-site-internet",
    "nav": "Création de site internet",
    "title": "Création de site internet professionnel | Jercat",
    "desc": "Création de site internet pour TPE, indépendants, commerçants et associations partout en France. Site vitrine dès 99 €, e-commerce. Devis gratuit sous 24 h.",
    "tag": "Création de site internet · Partout en France, à distance",
    "h1": "Création de site internet <em>professionnel.</em>",
    "sub": "Un site rapide, beau sur mobile et pensé pour que Google vous trouve. Pour les TPE, indépendants, commerçants, artisans et associations, partout en France. Un seul interlocuteur, un prix fixé avant de commencer.",
    "service_name": "Création de site internet",
    "min_price": "99",
    "sections": [
      ("Un site internet qui vous apporte des clients",
       "<p>Un site internet n'est pas une carte de visite posée sur le web : c'est l'endroit où vos futurs clients vérifient que vous êtes sérieux, comparent et décident de vous contacter. Je conçois chaque site avec un objectif simple : <strong>transformer les visiteurs en demandes de devis, en appels ou en ventes</strong>.</p>"
       "<p>Concrètement, cela veut dire un message clair dès le premier écran, des boutons de contact visibles partout, des pages qui se chargent en moins de deux secondes et un référencement Google préparé dès la conception.</p>"),
      ("Les types de sites que je crée",
       "<ul>"
       "<li><strong>Site vitrine</strong> : présenter votre activité, vos services, vos réalisations et être contacté. <a href=\"/creation-site-vitrine\">En savoir plus sur le site vitrine</a>.</li>"
       "<li><strong>Site e-commerce</strong> : vendre en ligne avec paiement sécurisé, gestion des stocks et suivi des commandes.</li>"
       "<li><strong>Landing page</strong> : une page unique et percutante pour une offre, un lancement ou une campagne publicitaire.</li>"
       "<li><strong>Site éditorial ou blog</strong> : attirer du trafic Google avec des guides et des articles.</li>"
       "<li><strong>Application web</strong> : un outil sur mesure (espace client, réservation, tableau de bord). <a href=\"/developpement-application-web\">Voir le développement d'application web</a>.</li>"
       "</ul>"),
      ("Ce qui est inclus dans chaque site",
       "<ul>"
       "<li>Design professionnel et 100 % adapté au mobile, à la tablette et à l'ordinateur.</li>"
       "<li>Textes structurés pour Google : titres, descriptions, balisage, données structurées.</li>"
       "<li>Formulaire de contact protégé contre le spam, bouton d'appel et liens vers vos réseaux.</li>"
       "<li>Hébergement rapide, certificat HTTPS, mise en ligne sur votre nom de domaine.</li>"
       "<li>Mentions légales et page de confidentialité (RGPD).</li>"
       "<li>Trois séries de corrections incluses, puis une prise en main pour être autonome.</li>"
       "</ul>"),
      ("Partout en France, à distance",
       "<p>Je travaille entièrement à distance : un premier appel ou une visio pour comprendre votre projet, une maquette à valider, puis une préversion en ligne que vous consultez depuis votre téléphone ou votre ordinateur. Vous n'avez pas besoin de vous déplacer, et vous parlez toujours à la même personne. J'ai par exemple réalisé le site d'un artisan basé en Belgique, <a href=\"/etudes-de-cas#fred-renovation\">Fred Rénovation</a>.</p>"),
      ("Combien coûte la création d'un site internet ?",
       "<p>Mes formules démarrent à <strong>99 €</strong> pour un site vitrine de 1 à 3 pages, <strong>199 €</strong> pour un site jusqu'à 8 pages avec blog, et <strong>300 €</strong> pour une boutique en ligne. Ces prix sont bas parce qu'il n'y a ni agence, ni locaux, ni commerciaux : vous ne payez que le travail. Le prix définitif est fixé dans un devis gratuit, avant tout démarrage, et vous payez 50 % à la commande, 50 % à la livraison. Les repères du marché sont détaillés dans le <a href=\"/prix-site-internet-2026\">guide des prix 2026</a>.</p>"),
    ],
    "steps": [("Échange gratuit", "Appel ou visio de 20 minutes pour cerner vos objectifs et votre budget."),
              ("Devis et maquette", "Un devis clair et une première maquette à valider."),
              ("Développement", "Préversion en ligne consultable à tout moment."),
              ("Mise en ligne", "Vérifications, référencement, prise en main et suivi.")],
    "faq": [
      ("Combien de temps faut-il pour créer un site internet ?", "Comptez environ 7 jours pour un site vitrine dès réception de vos textes et photos, et 2 à 4 semaines pour une boutique en ligne ou un site plus complet. Le délai est écrit dans le devis."),
      ("Est-ce que je serai propriétaire de mon site ?", "Oui. Le nom de domaine est à votre nom et le site vous appartient. Vous n'êtes lié par aucun abonnement obligatoire."),
      ("Je n'ai pas de textes ni de photos, est-ce un problème ?", "Non. Je vous envoie une trame de questions simples et je rédige les textes à partir de vos réponses. Des photos libres de droits peuvent compléter les vôtres."),
      ("Mon site sera-t-il visible sur Google ?", "Il est construit pour : structure, vitesse, balises et données structurées sont optimisées dès le départ, et je déclare le site à Google. Le positionnement dépend ensuite de la concurrence et du contenu publié."),
      ("Travaillez-vous avec des associations ?", "Oui, associations, indépendants, professions libérales, commerçants, artisans et TPE. Les formules d'entrée de gamme sont pensées pour les petits budgets."),
    ],
    "case": "aux-folies-burger",
  },
  {
    "slug": "creation-site-vitrine",
    "nav": "Création de site vitrine",
    "title": "Création de site vitrine dès 99 € | Jercat",
    "desc": "Site vitrine sur mesure, rapide et optimisé Google pour indépendants, artisans, commerçants et associations partout en France. Dès 99 €, livré en 7 jours.",
    "tag": "Site vitrine · Dès 99 € · Livré en 7 jours",
    "h1": "Création de <em>site vitrine.</em>",
    "sub": "Présentez votre activité, rassurez vos visiteurs et recevez des demandes de contact. Un site vitrine sur mesure, livré en 7 jours, partout en France.",
    "service_name": "Création de site vitrine",
    "min_price": "99",
    "sections": [
      ("À quoi sert un site vitrine ?",
       "<p>Un site vitrine présente votre entreprise, vos services, vos tarifs ou vos réalisations, et permet de vous contacter facilement. Il ne vend pas directement en ligne : il <strong>convainc</strong>. C'est le format idéal pour un artisan, un consultant, un thérapeute, un commerce de proximité, un restaurant ou une association.</p>"),
      ("Les pages d'un site vitrine efficace",
       "<ul>"
       "<li><strong>Accueil</strong> : qui vous êtes, ce que vous proposez, et un bouton de contact visible immédiatement.</li>"
       "<li><strong>Services ou prestations</strong> : une section ou une page par service, ce qui aide aussi le référencement.</li>"
       "<li><strong>Réalisations ou galerie</strong> : la preuve en images de la qualité de votre travail.</li>"
       "<li><strong>Avis clients</strong> : vos meilleurs témoignages, ou vos avis Google.</li>"
       "<li><strong>À propos</strong> : votre histoire et ce qui vous différencie.</li>"
       "<li><strong>Contact</strong> : formulaire, téléphone, horaires et zone d'intervention.</li>"
       "</ul>"),
      ("Les trois formules",
       "<ul>"
       "<li><strong>Essentiel, dès 99 €</strong> : site de 1 à 3 pages, design professionnel, formulaire de contact, mise en ligne incluse, livraison en 7 jours.</li>"
       "<li><strong>Pro, dès 199 €</strong> : jusqu'à 8 pages, design sur mesure, référencement Google optimisé, blog, galerie, formation et un mois de support.</li>"
       "<li><strong>Sur mesure</strong> : prise de rendez-vous, espace membre, plusieurs langues… chiffré dans un devis gratuit.</li>"
       "</ul>"
       "<p>Comparez avec les prix pratiqués en agence dans le <a href=\"/prix-site-internet-2026\">guide des prix d'un site internet en 2026</a>.</p>"),
      ("Un site vitrine pensé pour Google",
       "<p>Chaque page a un titre et une description uniques, une structure de titres logique, des images compressées et des données structurées qui aident Google à comprendre votre activité. Si vous visez une clientèle locale, j'ajoute votre zone d'intervention et je vous aide à configurer votre fiche Google Business Profile ; si vous visez toute la France, la stratégie repose sur des pages de services détaillées et des articles de blog.</p>"),
    ],
    "steps": [("Questionnaire", "Vous décrivez votre activité en quelques questions."),
              ("Maquette", "Première version visuelle sous quelques jours."),
              ("Corrections", "Trois séries de modifications incluses."),
              ("Mise en ligne", "Votre site sur votre nom de domaine, en HTTPS.")],
    "faq": [
      ("Pourquoi un site vitrine à 99 € ?", "Parce que je travaille seul, sans locaux ni commerciaux, avec des outils modernes qui vont vite. La formule Essentiel couvre 1 à 3 pages : idéal pour démarrer, et le site peut évoluer ensuite."),
      ("Y a-t-il des frais chaque mois ?", "Le nom de domaine et l'hébergement ont un coût annuel modeste, indiqué dans le devis. Il n'y a pas d'abonnement obligatoire pour le site lui-même."),
      ("Puis-je modifier mon site vitrine moi-même ?", "Oui, la formule Pro inclut une prise en main pour mettre à jour vos textes, photos et actualités. Sinon, je fais les modifications pour vous."),
      ("Le site sera-t-il adapté aux smartphones ?", "Oui, chaque site est conçu d'abord pour le mobile, où se trouve aujourd'hui la majorité des visiteurs."),
    ],
    "case": "fred-renovation",
  },
  {
    "slug": "developpeur-web-freelance",
    "nav": "Développeur web freelance",
    "title": "Développeur web freelance partout en France | Jercat",
    "desc": "Développeur web freelance à distance : sites internet, applications web, React, maintenance. Un seul interlocuteur, prix fixé d'avance, devis sous 24 h.",
    "tag": "Développeur web freelance · France entière",
    "h1": "Développeur web <em>freelance.</em>",
    "sub": "Sites internet, boutiques en ligne, applications web et automatisations : un développeur indépendant qui travaille directement avec vous, sans intermédiaire, partout en France.",
    "service_name": "Développement web freelance",
    "min_price": "99",
    "sections": [
      ("Pourquoi choisir un développeur freelance plutôt qu'une agence ?",
       "<ul>"
       "<li><strong>Un seul interlocuteur</strong> : la personne qui code votre site est celle qui vous répond. Pas de chef de projet, pas de sous-traitance cachée.</li>"
       "<li><strong>Des prix plus bas</strong> : pas de locaux ni d'équipe commerciale à financer.</li>"
       "<li><strong>De la réactivité</strong> : réponse sous 24 h, corrections rapides.</li>"
       "<li><strong>De la souplesse</strong> : un petit ajout ou une modification ne nécessite pas un nouveau bon de commande de trois pages.</li>"
       "</ul>"
       "<p>La contrepartie : un freelance gère un nombre limité de projets à la fois. C'est pourquoi je fixe un délai précis dans chaque devis, et je le tiens.</p>"),
      ("Ce que je développe",
       "<ul>"
       "<li><a href=\"/creation-site-internet\">Création de site internet</a> et <a href=\"/creation-site-vitrine\">site vitrine</a>.</li>"
       "<li><a href=\"/refonte-site-internet\">Refonte</a> et <a href=\"/maintenance-site-web\">maintenance de site web</a>.</li>"
       "<li><a href=\"/developpement-application-web\">Applications web</a> sur mesure : espaces clients, outils internes, réservations.</li>"
       "<li><a href=\"/automatisation-ia\">Automatisations et intégrations d'intelligence artificielle</a>.</li>"
       "<li>Développement <a href=\"/developpeur-react\">React</a>, <a href=\"/developpeur-javascript\">JavaScript</a> et <a href=\"/developpeur-full-stack\">full-stack</a> (Node.js, Firebase).</li>"
       "</ul>"),
      ("Mon parcours",
       "<p>Avant le web, j'ai passé près de vingt ans dans l'industrie et la logistique. J'en garde une approche concrète : un site doit servir à quelque chose de mesurable, être livré à la date prévue et être simple à utiliser pour des gens qui ont autre chose à faire. Je travaille avec des outils modernes (HTML, CSS, JavaScript, React, Node.js, Firebase, Vercel) qui donnent des sites rapides, sûrs et peu coûteux à héberger.</p>"),
      ("Tarifs d'un développeur web freelance",
       "<p>Sur les plateformes, les développeurs web freelances facturent généralement entre 250 et 550 € la journée. Je préfère un <strong>prix au projet</strong>, fixé dans le devis : vous savez exactement ce que vous payez avant de commencer. Sites vitrines dès 99 €, sites complets dès 199 €, boutiques en ligne dès 300 €, applications et automatisations sur devis.</p>"),
    ],
    "steps": [("Votre besoin", "Vous expliquez votre projet par téléphone, email ou formulaire."),
              ("Proposition", "Devis détaillé avec prix, délai et contenu exact."),
              ("Réalisation", "Développement avec préversion et points réguliers."),
              ("Suivi", "Mise en ligne, prise en main, support.")],
    "faq": [
      ("Travaillez-vous uniquement à distance ?", "Oui, pour la grande majorité des projets : appels, visios, emails et préversion en ligne suffisent. Je peux me déplacer dans l'Aisne et les environs si nécessaire."),
      ("Êtes-vous disponible pour une mission courte ?", "Oui, pour une correction, une nouvelle page, une intégration ou une petite fonctionnalité. Décrivez le besoin dans le formulaire, je vous réponds sous 24 h."),
      ("Signez-vous un devis et une facture ?", "Oui, chaque projet fait l'objet d'un devis détaillé avant démarrage puis d'une facture, avec paiement en deux fois."),
      ("Pouvez-vous reprendre un site créé par quelqu'un d'autre ?", "Oui. Je fais d'abord un état des lieux, puis je vous propose de le corriger, de le maintenir ou de le refaire selon ce qui est le plus rentable pour vous."),
    ],
    "case": "bon-plan-et-reduction",
  },
  {
    "slug": "developpeur-react",
    "nav": "Développeur React",
    "title": "Développeur React freelance | Jercat",
    "desc": "Développeur React freelance : applications web, espaces clients et interfaces rapides avec React, Firebase et Node.js. À distance, partout en France.",
    "tag": "React · Firebase · Node.js · Vercel",
    "h1": "Développeur <em>React</em> freelance.",
    "sub": "Des interfaces rapides, fluides et faciles à faire évoluer : applications web, tableaux de bord, espaces clients et sites dynamiques développés avec React.",
    "service_name": "Développement React",
    "min_price": None,
    "sections": [
      ("Quand choisir React pour votre projet ?",
       "<p>React est la bibliothèque JavaScript la plus utilisée pour créer des interfaces web interactives. Elle est particulièrement adaptée quand votre projet doit <strong>réagir en temps réel</strong> aux actions des utilisateurs : filtres, formulaires en plusieurs étapes, tableaux de bord, espaces membres, réservations, calculateurs ou paniers.</p>"
       "<p>Pour un simple site vitrine, React n'est pas toujours nécessaire : un site statique bien construit est souvent plus rapide et moins cher. Je vous conseille la solution la plus simple qui répond à votre besoin.</p>"),
      ("Ce que je développe avec React",
       "<ul>"
       "<li>Applications web et outils métier (gestion, suivi, planning, devis).</li>"
       "<li>Espaces clients et back-offices avec authentification.</li>"
       "<li>Simulateurs, configurateurs et calculateurs de prix.</li>"
       "<li>Interfaces connectées à des API et à l'intelligence artificielle.</li>"
       "<li>Migration d'une interface vieillissante vers React.</li>"
       "</ul>"),
      ("Une stack moderne et économique",
       "<p>J'associe React à <strong>Firebase</strong> (base de données temps réel, authentification, stockage), à <strong>Node.js</strong> pour les traitements côté serveur et à <strong>Vercel</strong> pour l'hébergement. Résultat : des applications rapides, sécurisées, qui montent en charge sans serveur à administrer et avec des coûts d'hébergement souvent nuls ou très faibles au démarrage.</p>"),
      ("Exemple concret",
       "<p>Pour le restaurant <a href=\"/etudes-de-cas#aux-folies-burger\">Aux Folie's Burger</a>, j'ai réalisé un site avec menu interactif et système de fidélité, appuyé sur Firebase et Vercel. Voir aussi le <a href=\"/developpement-application-web\">développement d'application web</a> et le <a href=\"/developpeur-full-stack\">développement full-stack</a>.</p>"),
    ],
    "steps": [("Cadrage", "Fonctionnalités, utilisateurs, priorités."),
              ("Maquettes", "Écrans principaux validés avant de coder."),
              ("Développement", "Livraisons régulières sur une préversion."),
              ("Mise en production", "Déploiement, documentation, support.")],
    "faq": [
      ("Faites-vous des missions React en renfort d'une équipe ?", "Je privilégie les projets complets pour des TPE, PME et associations. Pour un renfort ponctuel sur une base existante, décrivez le besoin : je vous dis honnêtement si je suis la bonne personne."),
      ("Utilisez-vous Next.js ?", "Selon le projet. Pour un site qui doit être très bien référencé sur Google, un rendu côté serveur ou statique est préférable ; je choisis l'outil adapté au besoin."),
      ("Combien coûte une application React ?", "Cela dépend du nombre d'écrans et de fonctionnalités. Le devis est gratuit et détaille chaque élément, sans engagement."),
    ],
    "case": "aux-folies-burger",
  },
  {
    "slug": "developpeur-javascript",
    "nav": "Développeur JavaScript",
    "title": "Développeur JavaScript freelance | Jercat",
    "desc": "Développeur JavaScript freelance : simulateurs, formulaires, intégrations d'API, corrections et performance. Projets à distance partout en France.",
    "tag": "JavaScript · HTML · CSS · API",
    "h1": "Développeur <em>JavaScript</em> freelance.",
    "sub": "Formulaires intelligents, simulateurs, animations, connexions à des API, corrections de bugs : du JavaScript propre et rapide pour rendre votre site utile.",
    "service_name": "Développement JavaScript",
    "min_price": None,
    "sections": [
      ("Ce que le JavaScript apporte à votre site",
       "<p>Le JavaScript est le langage qui rend un site interactif. Bien utilisé, il améliore l'expérience de vos visiteurs et le taux de conversion : un simulateur de prix qui donne une estimation immédiate, un formulaire qui guide pas à pas, une galerie fluide, un module de réservation ou un chat.</p>"
       "<p>Mal utilisé, il alourdit les pages et pénalise le référencement. Je développe en <strong>JavaScript moderne et léger</strong>, sans bibliothèques inutiles, pour garder des pages qui se chargent vite.</p>"),
      ("Exemples de développements",
       "<ul>"
       "<li>Simulateurs et calculateurs (prix, gains, devis instantané).</li>"
       "<li>Formulaires en plusieurs étapes avec vérification des champs et protection anti-spam.</li>"
       "<li>Intégration d'API : paiement, cartes, calendrier, CRM, emailing, intelligence artificielle.</li>"
       "<li>Animations et effets visuels soignés, sans ralentir le site.</li>"
       "<li>Corrections de bugs et optimisation des performances (Core Web Vitals).</li>"
       "</ul>"),
      ("Un exemple : un site éditorial avec simulateur",
       "<p>Sur <a href=\"/etudes-de-cas#bon-plan-et-reduction\">Bon plan et réduction</a>, un site d'environ 40 pages de guides et comparatifs, j'ai développé un simulateur de gains en JavaScript, un mode sombre et des pages optimisées pour Google.</p>"),
      ("Performance et référencement",
       "<p>Google mesure la rapidité et la stabilité des pages. Je charge le JavaScript uniquement là où il sert, je compresse les fichiers et je vérifie les scores de performance avant chaque mise en ligne. Pour une application plus complète, voir le <a href=\"/developpeur-react\">développement React</a>.</p>"),
    ],
    "steps": [("Diagnostic", "Ce qui doit être créé, corrigé ou accéléré."),
              ("Devis", "Prix et délai fixés avant de commencer."),
              ("Développement", "Tests sur mobile et ordinateur."),
              ("Livraison", "Mise en ligne et contrôle des performances.")],
    "faq": [
      ("Pouvez-vous ajouter une fonctionnalité à mon site existant ?", "Oui, quel que soit l'outil utilisé (site codé, WordPress, Shopify…), dans la mesure où j'ai accès au code ou à l'administration."),
      ("Mon site est lent à cause du JavaScript, que faire ?", "Je fais un audit des scripts chargés, je supprime ceux qui ne servent pas et je différencie le chargement des autres. Le gain est souvent visible immédiatement."),
      ("Travaillez-vous avec TypeScript ?", "Selon le projet. Pour une petite fonctionnalité, du JavaScript moderne suffit ; pour une application plus grande, le typage peut être utile."),
    ],
    "case": "bon-plan-et-reduction",
  },
  {
    "slug": "developpement-application-web",
    "nav": "Développement d'application web",
    "title": "Développement d'application web sur mesure | Jercat",
    "desc": "Application web sur mesure pour TPE, PME et associations : outil métier, espace client, réservation, IA. Partout en France, devis gratuit sous 24 h.",
    "tag": "Application web · Outil métier · Espace client",
    "h1": "Développement <em>d'application web.</em>",
    "sub": "Remplacez les tableurs, les papiers et les tâches répétitives par un outil web simple, conçu pour votre façon de travailler et accessible depuis n'importe quel appareil.",
    "service_name": "Développement d'application web",
    "min_price": None,
    "sections": [
      ("Une application web, pour quoi faire ?",
       "<p>Une application web fonctionne dans le navigateur, sur ordinateur, tablette ou téléphone, sans installation. Elle sert à <strong>gérer, suivre ou automatiser</strong> une partie de votre activité : prises de rendez-vous, commandes, devis, stocks, planning d'équipe, suivi de chantiers, adhésions d'une association, programme de fidélité…</p>"),
      ("Exemples d'applications",
       "<ul>"
       "<li><strong>Espace client</strong> : vos clients consultent leurs documents, commandes ou rendez-vous.</li>"
       "<li><strong>Outil interne</strong> : un tableau de bord qui centralise vos données au lieu de dix fichiers Excel.</li>"
       "<li><strong>Réservation et planning</strong> : créneaux, rappels automatiques, gestion des annulations.</li>"
       "<li><strong>Back-office e-commerce</strong> : stocks, produits, commandes.</li>"
       "<li><strong>Application avec IA</strong> : génération de textes, de devis ou de visuels, assistant qui répond aux questions. Voir l'<a href=\"/automatisation-ia\">automatisation IA</a>.</li>"
       "</ul>"),
      ("Une méthode qui limite les risques",
       "<p>Le piège classique d'une application sur mesure, c'est le projet qui gonfle et qui ne se termine jamais. Je commence par une <strong>première version utile</strong> avec les fonctions essentielles, mise en service rapidement, puis on ajoute le reste selon l'usage réel. Vous payez par étape, et vous voyez l'application avancer sur une préversion.</p>"),
      ("Technologies",
       "<p>React pour l'interface, Firebase ou Node.js pour les données et la logique serveur, Vercel pour l'hébergement. Ce sont des outils éprouvés, sécurisés et peu coûteux à faire tourner. En savoir plus sur le <a href=\"/developpeur-full-stack\">développement full-stack</a>.</p>"),
    ],
    "steps": [("Atelier", "On liste les tâches à simplifier et les utilisateurs."),
              ("Première version", "Les fonctions essentielles, livrées vite."),
              ("Améliorations", "Ajouts selon l'usage réel."),
              ("Maintenance", "Corrections, sauvegardes, évolutions.")],
    "faq": [
      ("Combien coûte une application web sur mesure ?", "Le prix dépend du nombre d'écrans et de règles métier. Je propose un devis par étapes, en commençant par une première version utile, pour maîtriser votre budget."),
      ("Mes données seront-elles en sécurité ?", "Oui : accès protégé par identifiant, données hébergées chez des fournisseurs reconnus, règles de sécurité sur la base de données et sauvegardes."),
      ("L'application fonctionnera-t-elle sur téléphone ?", "Oui, elle est conçue pour le mobile et peut s'installer sur l'écran d'accueil comme une application."),
      ("Qui est propriétaire du code ?", "Vous. Le code et les données vous appartiennent, et je vous remets les accès."),
    ],
    "case": "bi-by-doris",
  },
  {
    "slug": "automatisation-ia",
    "nav": "Automatisation IA",
    "title": "Automatisation IA pour TPE et PME | Jercat",
    "desc": "Automatisation IA pour TPE et PME : assistant sur votre site, tri des demandes, relances, devis et contenus automatiques. Gagnez des heures chaque semaine.",
    "tag": "Intelligence artificielle · Automatisation · Chatbot",
    "h1": "Automatisation <em>&amp; intelligence artificielle.</em>",
    "sub": "Réponses aux demandes, relances, devis, contenus, tri des emails : confiez les tâches répétitives à des automatisations et à l'IA, et gardez votre temps pour vos clients.",
    "service_name": "Automatisation et intelligence artificielle",
    "min_price": None,
    "sections": [
      ("Ce que l'IA peut faire pour une petite entreprise",
       "<p>L'intelligence artificielle n'est plus réservée aux grands groupes. Pour une TPE, un indépendant ou une association, elle sert surtout à <strong>gagner du temps sur les tâches qui reviennent tous les jours</strong> :</p>"
       "<ul>"
       "<li>Un assistant sur votre site qui répond aux questions fréquentes, 24 h/24, et transmet les demandes qualifiées.</li>"
       "<li>Le tri et le résumé des emails et des demandes de devis.</li>"
       "<li>La préparation de devis, de comptes rendus ou de réponses types à partir de vos informations.</li>"
       "<li>La rédaction de brouillons de publications, de fiches produits ou de descriptions.</li>"
       "<li>La création de visuels et de vidéos courtes pour les réseaux sociaux.</li>"
       "</ul>"),
      ("Automatiser sans tout changer",
       "<p>L'objectif n'est pas de remplacer vos outils, mais de les <strong>connecter</strong> : votre formulaire de contact, votre messagerie, votre agenda, votre tableur ou votre CRM. Une demande arrive sur le site ? Elle est enregistrée, vous recevez une notification, le client reçoit une confirmation, et une relance part automatiquement si personne n'a répondu.</p>"),
      ("Des projets IA déjà réalisés",
       "<p>J'ai développé des applications web qui intègrent l'IA : un générateur de publicités qui rédige des annonces à partir de quelques informations sur l'entreprise, et un générateur de vidéos courtes pour les réseaux sociaux. Les clés d'accès aux services d'IA restent toujours côté serveur, jamais visibles dans le navigateur.</p>"),
      ("Un démarrage simple et mesurable",
       "<p>On commence par identifier une ou deux tâches qui vous coûtent le plus de temps chaque semaine. Je vous propose une automatisation chiffrée, mise en place rapidement, puis on mesure le temps gagné avant d'aller plus loin. Les données personnelles sont traitées dans le respect du RGPD, et vous gardez la main sur ce qui est envoyé à vos clients.</p>"),
    ],
    "steps": [("Diagnostic", "Les tâches répétitives qui vous coûtent du temps."),
              ("Proposition", "Une automatisation chiffrée et son gain attendu."),
              ("Mise en place", "Connexion de vos outils et tests."),
              ("Mesure", "Temps gagné, ajustements, étape suivante.")],
    "faq": [
      ("Faut-il des compétences techniques pour utiliser ces automatisations ?", "Non. Je les configure et je vous explique comment elles fonctionnent. Au quotidien, vous continuez à utiliser vos outils habituels."),
      ("Un chatbot peut-il dire n'importe quoi à mes clients ?", "Je le limite à vos informations (services, tarifs, horaires, FAQ) et je prévois un passage de relais vers vous dès que la question sort de ce cadre."),
      ("Combien coûte une automatisation IA ?", "Une première automatisation simple reste abordable ; le coût des services d'IA utilisés est généralement de quelques euros par mois pour une petite entreprise. Tout est chiffré dans le devis."),
      ("Mes données sont-elles protégées ?", "Je n'envoie aux services d'IA que les informations nécessaires, je documente les traitements et je vous aide à mettre à jour votre politique de confidentialité."),
    ],
    "case": "bon-plan-et-reduction",
  },
  {
    "slug": "maintenance-site-web",
    "nav": "Maintenance de site web",
    "title": "Maintenance de site web : sécurité et mises à jour | Jercat",
    "desc": "Maintenance de site web : mises à jour, sauvegardes, sécurité, corrections et petites évolutions. Pour TPE et associations partout en France.",
    "tag": "Maintenance · Sécurité · Évolutions",
    "h1": "Maintenance de <em>site web.</em>",
    "sub": "Un site qui reste rapide, sécurisé et à jour, sans que vous ayez à vous en occuper. Corrections, mises à jour, sauvegardes et petites évolutions, avec un interlocuteur qui répond.",
    "service_name": "Maintenance de site web",
    "min_price": None,
    "sections": [
      ("Pourquoi un site doit être entretenu",
       "<p>Un site internet n'est jamais vraiment terminé. Les navigateurs évoluent, les extensions vieillissent, les certificats expirent, les formulaires attirent du spam, et Google favorise les sites rapides et à jour. Un site laissé à l'abandon finit par <strong>tomber en panne, se faire pirater ou disparaître des résultats</strong>.</p>"),
      ("Ce que comprend la maintenance",
       "<ul>"
       "<li>Mises à jour techniques (CMS, extensions, bibliothèques).</li>"
       "<li>Sauvegardes régulières et restauration en cas de problème.</li>"
       "<li>Surveillance de la disponibilité et du certificat HTTPS.</li>"
       "<li>Vérification du formulaire de contact et protection anti-spam.</li>"
       "<li>Corrections de bugs et d'affichage.</li>"
       "<li>Petites modifications de contenu : textes, photos, horaires, tarifs.</li>"
       "<li>Contrôle des performances et du référencement (Search Console).</li>"
       "</ul>"),
      ("Pour quels sites ?",
       "<p>Les sites que j'ai créés, bien sûr, mais aussi les sites existants réalisés par une autre personne ou une agence, qu'ils soient codés à la main, sous WordPress ou sur une autre solution. Je commence par un état des lieux gratuit pour vous dire ce qui doit être corrigé en priorité. Si le site est trop daté, une <a href=\"/refonte-site-internet\">refonte</a> peut revenir moins cher que de le réparer.</p>"),
      ("Une formule adaptée à votre site",
       "<p>Intervention ponctuelle quand vous en avez besoin, ou suivi régulier avec un nombre de modifications inclus : le format et le prix sont fixés dans un devis gratuit, selon la taille et la technologie de votre site.</p>"),
    ],
    "steps": [("État des lieux", "Sécurité, vitesse, formulaire, référencement."),
              ("Corrections", "Les problèmes urgents sont réglés d'abord."),
              ("Suivi", "Mises à jour et sauvegardes régulières."),
              ("Évolutions", "Vos demandes traitées sous 24 à 72 h.")],
    "faq": [
      ("Mon site a été créé par quelqu'un d'autre, pouvez-vous le maintenir ?", "Oui, dès que j'ai les accès (hébergement, nom de domaine, administration). Je fais d'abord un état des lieux."),
      ("Que se passe-t-il si mon site tombe en panne ?", "Je diagnostique la cause, je restaure la dernière sauvegarde si nécessaire et je vous explique ce qui s'est passé."),
      ("Puis-je demander des modifications de contenu ?", "Oui, les petites modifications (textes, photos, horaires, tarifs) font partie de la maintenance."),
      ("Suis-je engagé sur une longue durée ?", "Non, vous pouvez choisir des interventions ponctuelles. Un suivi régulier est proposé pour ceux qui préfèrent ne plus y penser."),
    ],
    "case": "tanjiro59",
  },
  {
    "slug": "refonte-site-internet",
    "nav": "Refonte de site internet",
    "title": "Refonte de site internet sans perdre Google | Jercat",
    "desc": "Refonte de site internet moderne, rapide et sécurisée, en conservant votre référencement Google. Partout en France, devis gratuit sous 24 h.",
    "tag": "Refonte · Modernisation & performance",
    "h1": "Refonte de <em>site internet.</em>",
    "sub": "Votre site a quelques années, s'affiche mal sur mobile ou ne vous apporte plus de clients ? Je le modernise en préservant votre place sur Google, où que vous soyez en France.",
    "service_name": "Refonte de site internet",
    "min_price": "99",
    "sections": [
      ("Les signes qu'il est temps de refaire votre site",
       "<ul><li>Il s'affiche mal ou est difficile à utiliser sur smartphone.</li><li>Il met plusieurs secondes à se charger.</li><li>Le navigateur indique « non sécurisé » (pas de HTTPS).</li><li>Le design date et ne reflète plus la qualité de votre travail.</li><li>Vous ne pouvez pas modifier vos contenus sans aide.</li><li>Il ne vous apporte presque plus de demandes de contact.</li></ul>"),
      ("Moderniser sans perdre votre référencement",
       "<p>Le principal risque d'une refonte est de perdre les positions acquises sur Google. Pour l'éviter, je recense les pages existantes qui reçoivent des visites, je conserve les adresses quand c'est possible et je mets en place des <strong>redirections permanentes (301)</strong> pour celles qui changent. Les textes qui fonctionnent sont gardés et améliorés plutôt que supprimés.</p>"),
      ("Ce que la refonte apporte",
       "<ul><li><strong>Design moderne</strong> et cohérent avec votre image.</li><li><strong>Affichage parfait sur mobile</strong>, tablette et ordinateur.</li><li><strong>Chargement rapide</strong>, apprécié des visiteurs et de Google.</li><li><strong>HTTPS</strong> et bonnes pratiques de sécurité.</li><li><strong>Parcours de contact simplifié</strong> : boutons d'appel et de devis visibles, formulaire court.</li></ul>"),
      ("Déroulement et prix",
       "<p>Analyse du site actuel, maquette, développement sur une préversion séparée (l'ancien site reste en ligne), puis bascule sur votre adresse habituelle avec vérification des redirections. Trois séries de corrections sont incluses. Une refonte se chiffre comme une création, à partir de 99 € pour un petit site vitrine ; votre tarif exact figure dans un devis gratuit. Pour l'entretien ensuite, voir la <a href=\"/maintenance-site-web\">maintenance de site web</a>.</p>"),
    ],
    "steps": [("Audit", "Pages qui comptent, problèmes, opportunités."),
              ("Maquette", "Nouveau design validé avec vous."),
              ("Préversion", "Le nouveau site en test, l'ancien reste en ligne."),
              ("Bascule", "Mise en ligne, redirections 301, suivi Google.")],
    "faq": [
      ("Vais-je perdre mon référencement Google avec une refonte ?", "Pas si la refonte est bien préparée : conservation des adresses quand c'est possible, redirections 301 pour celles qui changent et reprise des contenus qui fonctionnent. C'est une étape que je traite systématiquement."),
      ("Puis-je garder mon nom de domaine actuel ?", "Oui. Le nouveau site est mis en ligne sur votre adresse habituelle, vos clients et Google le retrouvent au même endroit."),
      ("Mon site restera-t-il en ligne pendant les travaux ?", "Oui. Le nouveau site est développé sur une préversion séparée, et l'ancien reste en ligne jusqu'à la bascule finale."),
      ("Pouvez-vous refaire un site WordPress ?", "Oui, soit en restant sous WordPress, soit en passant à un site codé plus rapide si vous n'avez pas besoin de modifier souvent le contenu."),
    ],
    "case": "fred-renovation",
  },
  {
    "slug": "developpeur-full-stack",
    "nav": "Développeur full-stack",
    "title": "Développeur full-stack freelance React Node | Jercat",
    "desc": "Développeur full-stack freelance : interface React, serveur Node.js, base Firebase, API et hébergement Vercel. Un seul développeur pour tout votre projet.",
    "tag": "Full-stack · React · Node.js · Firebase",
    "h1": "Développeur <em>full-stack</em> freelance.",
    "sub": "L'interface, le serveur, la base de données et la mise en ligne : un seul développeur pour l'ensemble de votre projet web, avec une vision complète et un seul interlocuteur.",
    "service_name": "Développement full-stack",
    "min_price": None,
    "sections": [
      ("Full-stack, ça veut dire quoi ?",
       "<p>Un projet web a deux faces : le <strong>front-end</strong>, ce que voit l'utilisateur (pages, boutons, formulaires), et le <strong>back-end</strong>, ce qui travaille en coulisses (base de données, comptes utilisateurs, paiements, envois d'emails, connexions à d'autres services). Un développeur full-stack s'occupe des deux, ce qui évite les allers-retours entre prestataires et les problèmes de compatibilité.</p>"),
      ("Ma stack technique",
       "<ul>"
       "<li><strong>Front-end</strong> : HTML, CSS, JavaScript, <a href=\"/developpeur-react\">React</a>.</li>"
       "<li><strong>Back-end</strong> : Node.js, fonctions serverless, API REST.</li>"
       "<li><strong>Données</strong> : Firebase (Firestore, authentification, stockage).</li>"
       "<li><strong>Hébergement</strong> : Vercel, avec HTTPS et déploiement automatique.</li>"
       "<li><strong>Intégrations</strong> : paiement en ligne, emails, services d'IA, outils tiers.</li>"
       "</ul>"),
      ("Projets typiques",
       "<p>Une boutique avec espace administrateur et gestion des stocks, comme <a href=\"/etudes-de-cas#bi-by-doris\">Bi by Doris</a> ; un site avec programme de fidélité, comme <a href=\"/etudes-de-cas#aux-folies-burger\">Aux Folie's Burger</a> ; une application métier ou un outil avec IA intégrée. Pour en savoir plus, voir le <a href=\"/developpement-application-web\">développement d'application web</a>.</p>"),
      ("Sécurité et coûts maîtrisés",
       "<p>Les clés d'accès aux services restent côté serveur, les règles d'accès aux données sont configurées dès le départ, et l'hébergement serverless évite d'administrer une machine. Pour une petite structure, les coûts d'hébergement restent souvent nuls ou très faibles au démarrage.</p>"),
    ],
    "steps": [("Architecture", "Choix des outils selon votre besoin réel."),
              ("Interface", "Écrans validés avant développement."),
              ("Back-end", "Données, sécurité, intégrations."),
              ("Mise en ligne", "Déploiement, tests, documentation.")],
    "faq": [
      ("Pourquoi un seul développeur pour tout le projet ?", "Parce qu'il connaît l'ensemble du système : moins de pertes d'information, des corrections plus rapides et un seul interlocuteur responsable."),
      ("Pouvez-vous intervenir sur un projet existant ?", "Oui, après un état des lieux du code, des accès et de l'hébergement."),
      ("Proposez-vous la maintenance après la livraison ?", "Oui, voir la maintenance de site web : corrections, mises à jour et évolutions."),
    ],
    "case": "bi-by-doris",
  },
]

# --------------------------------------------------------------------------------------
# ÉTUDES DE CAS (uniquement des faits connus — compléter les champs « à compléter »)
# --------------------------------------------------------------------------------------
CASES = [
  {"id": "fred-renovation", "name": "Fred Rénovation", "type": "Site vitrine · Artisan rénovation",
   "url": "https://fredrenovation.vercel.app/", "img": "realisations/fred-renovation.webp",
   "where": "Artisan basé en Belgique",
   "need": "Un artisan de la rénovation voulait présenter son savoir-faire, montrer ses chantiers et recevoir des demandes de devis en ligne.",
   "solution": ["Site vitrine professionnel avec galerie de réalisations", "Formulaire de demande de devis en ligne", "Référencement local optimisé (balises, données structurées, zone d'intervention)", "Affichage optimisé sur mobile"],
   "tech": "Hébergement Vercel",
   "result": "Site en ligne, avec un parcours de contact direct depuis chaque page."},
  {"id": "aux-folies-burger", "name": "Aux Folie's Burger", "type": "Site vitrine + fidélité · Restaurant",
   "url": "https://aux-folie-s-burger.vercel.app/", "img": "realisations/aux-folies-burger.webp",
   "where": "Restaurant burger",
   "need": "Un restaurant avait besoin de mettre en valeur son menu et de fidéliser ses clients.",
   "solution": ["Site vitrine avec menu interactif", "Système de fidélité", "Base de données Firebase", "Hébergement Vercel rapide et sécurisé"],
   "tech": "JavaScript, Firebase, Vercel",
   "result": "Menu consultable sur mobile et programme de fidélité intégré au site."},
  {"id": "bi-by-doris", "name": "Bi by Doris", "type": "E-commerce · Mode & accessoires",
   "url": "https://bi-by-doris.vercel.app/", "img": "realisations/bi-by-doris.webp",
   "where": "Boutique en ligne",
   "need": "Une boutique de mode et d'accessoires voulait vendre en ligne et gérer elle-même ses produits.",
   "solution": ["Boutique en ligne avec paiement sécurisé", "Gestion des stocks", "Espace administrateur", "Fiches produits optimisées"],
   "tech": "Hébergement Vercel",
   "result": "Boutique opérationnelle, gérable sans compétence technique."},
  {"id": "bon-plan-et-reduction", "name": "Bon plan et réduction", "type": "Site éditorial · SEO",
   "url": "https://plateforme-revenus.vercel.app/", "img": "realisations/bon-plan-et-reduction.webp",
   "where": "Site éditorial national",
   "need": "Créer un site de contenu capable d'attirer des visiteurs depuis Google sur des sujets cashback et parrainage.",
   "solution": ["Près de 40 pages de guides, comparatifs et fiches marchands", "Simulateur de gains en JavaScript", "Vidéos tutoriels et mode sombre", "Optimisation SEO de chaque page"],
   "tech": "JavaScript, hébergement Vercel",
   "result": "Une architecture éditoriale complète, conçue pour le référencement naturel."},
  {"id": "tanjiro59", "name": "Tanjiro59", "type": "Site créateur · YouTube",
   "url": "https://tanjiro59.vercel.app/", "img": "realisations/tanjiro59.webp",
   "where": "Créateur de contenu",
   "need": "Un créateur YouTube voulait un site à l'image de sa chaîne.",
   "solution": ["Identité visuelle cyberpunk", "Animation d'introduction sur mesure", "Liens vers les contenus et réseaux"],
   "tech": "Hébergement Vercel",
   "result": "Un site au style marqué, cohérent avec l'univers de la chaîne."},
  {"id": "chatastrophe-studio", "name": "Chatastrophe Studio", "type": "Application web · Vidéo",
   "url": "https://generator.jercat.fr/", "img": "realisations/chatastrophe-studio.webp",
   "where": "Projet personnel — outil grand public",
   "need": "Permettre à n'importe qui de créer en quelques clics des vidéos humoristiques de chats pour TikTok, YouTube Shorts et Instagram Reels.",
   "solution": ["Générateur de scénarios absurdes (bibliothèque d'idées ou idée libre)", "Chat animé personnalisable, voix de chat et sous-titres mot par mot", "Mode viral : accroche, coupes rapides, score de viralité, hashtags", "Export vidéo, sous-titres .srt et script .txt, génération directement dans le navigateur"],
   "tech": "JavaScript, fonctions serverless Vercel (écriture du script par IA en option)",
   "result": "Une application web complète, utilisable sur ordinateur et mobile, sans installation."},
]

# --------------------------------------------------------------------------------------
# BLOG — articles publiés
# --------------------------------------------------------------------------------------
ARTICLES = [
  {
    "slug": "site-vitrine-ou-site-e-commerce",
    "title": "Site vitrine ou site e-commerce : lequel choisir ?",
    "h1": "Site vitrine ou site e-commerce : <em>lequel choisir ?</em>",
    "desc": "Site vitrine ou boutique en ligne ? Différences, prix, délais et exemples concrets pour choisir le bon site pour votre entreprise ou votre association.",
    "date": "2026-11-10", "read": "6 min", "cat": "Choisir son site",
    "related": ["creation-site-vitrine", "creation-site-internet"],
    "body": [
      ("La différence en une phrase", "<p>Un <strong>site vitrine</strong> présente votre activité et vous fait contacter ; un <strong>site e-commerce</strong> vend directement en ligne, avec paiement et gestion des commandes. Le premier convainc, le second encaisse.</p>"),
      ("Quand un site vitrine suffit", "<ul><li>Vous vendez un service sur devis (artisan, consultant, prestataire).</li><li>Vos clients doivent vous appeler ou venir sur place (restaurant, salon, cabinet).</li><li>Vous êtes une association qui veut informer et recruter des adhérents.</li><li>Vous débutez et voulez une présence professionnelle rapidement, avec un petit budget.</li></ul><p>Un site vitrine peut quand même inclure une prise de rendez-vous, un formulaire de devis détaillé ou un menu interactif.</p>"),
      ("Quand passer à l'e-commerce", "<ul><li>Vous vendez des produits physiques ou numériques à des clients qui ne viennent pas en magasin.</li><li>Vous recevez déjà des commandes par message et passez du temps à les gérer à la main.</li><li>Vous voulez vendre en dehors de vos horaires d'ouverture et au-delà de votre zone.</li></ul>"),
      ("Prix et délais", "<p>À titre indicatif, mes formules commencent à 99 € pour un site vitrine de 1 à 3 pages et à 300 € pour une boutique en ligne ; une boutique demande plus de travail (fiches produits, paiement, livraison, conditions de vente). Comptez environ 7 jours pour un site vitrine et 2 à 4 semaines pour une boutique. Les repères du marché sont détaillés dans le <a href=\"/prix-site-internet-2026\">guide des prix 2026</a>.</p>"),
      ("La solution intermédiaire", "<p>Beaucoup d'entreprises commencent par un site vitrine bien référencé, puis ajoutent une petite boutique quand la demande est là. C'est souvent le choix le plus rentable : vous testez l'intérêt de vos clients sans investir tout de suite dans une boutique complète.</p>"),
    ],
  },
  {
    "slug": "cahier-des-charges-site-internet",
    "title": "Cahier des charges site internet : 10 questions",
    "h1": "Cahier des charges <em>d'un site internet.</em>",
    "desc": "Comment rédiger le cahier des charges de votre site internet en 10 questions simples, pour obtenir des devis comparables et éviter les mauvaises surprises.",
    "date": "2026-11-10", "read": "7 min", "cat": "Préparer son projet",
    "related": ["creation-site-internet", "developpement-application-web"],
    "body": [
      ("Pourquoi un cahier des charges ?", "<p>Sans description claire, chaque prestataire imagine un projet différent, et vous recevez des devis impossibles à comparer. Un cahier des charges n'a pas besoin d'être long : une ou deux pages qui répondent aux questions ci-dessous suffisent pour une TPE ou une association.</p>"),
      ("Les 10 questions à vous poser", "<ol><li><strong>Qui êtes-vous ?</strong> Activité, clients, ce qui vous différencie.</li><li><strong>À quoi doit servir le site ?</strong> Recevoir des devis, vendre, informer, recruter.</li><li><strong>Qui sont vos visiteurs ?</strong> Particuliers, professionnels, zone géographique.</li><li><strong>Quelles pages ?</strong> Listez-les : accueil, services, réalisations, contact…</li><li><strong>Quelles fonctionnalités ?</strong> Formulaire, rendez-vous, paiement, espace client, blog.</li><li><strong>Qui fournit les contenus ?</strong> Textes, photos, logo : vous, ou le prestataire.</li><li><strong>Quels sites aimez-vous ?</strong> Deux ou trois exemples, et pourquoi.</li><li><strong>Faut-il modifier le site soi-même ?</strong> Souvent, rarement, jamais.</li><li><strong>Quel budget ?</strong> Une fourchette évite de perdre du temps des deux côtés.</li><li><strong>Quel délai ?</strong> Une date de lancement, un salon, une ouverture.</li></ol>"),
      ("Les erreurs à éviter", "<ul><li>Demander « un site comme Amazon » sans préciser les fonctions vraiment utiles.</li><li>Oublier qui sera propriétaire du nom de domaine et du site.</li><li>Ne pas prévoir l'après : maintenance, mises à jour, modifications.</li><li>Négliger le référencement : il se prépare dès la conception.</li></ul>"),
      ("Pas le temps de l'écrire ?", "<p>Le formulaire de devis du site reprend l'essentiel de ces questions. Remplissez-le en trois champs, je complète avec vous lors d'un échange gratuit et je vous envoie un devis détaillé sous 24 h. Pour un outil plus complexe, voir le <a href=\"/developpement-application-web\">développement d'application web</a>.</p>"),
    ],
  },
  {
    "slug": "automatiser-son-entreprise-avec-l-ia",
    "title": "Automatiser son entreprise avec l'IA : 10 tâches",
    "h1": "Automatiser son entreprise <em>avec l'IA.</em>",
    "desc": "10 tâches qu'une TPE, un indépendant ou une association peut automatiser avec l'intelligence artificielle en 2026, et les précautions à prendre.",
    "date": "2026-11-10", "read": "8 min", "cat": "IA & automatisation",
    "related": ["automatisation-ia", "developpement-application-web"],
    "body": [
      ("Commencer petit", "<p>L'automatisation la plus rentable est souvent la plus simple : une tâche que vous faites tous les jours, toujours de la même manière. Notez pendant une semaine ce qui vous prend du temps sans demander de réflexion : c'est votre liste de départ.</p>"),
      ("10 tâches à automatiser", "<ol><li>Répondre aux questions fréquentes sur votre site (horaires, tarifs, délais).</li><li>Accuser réception des demandes de devis et les enregistrer dans un tableau.</li><li>Relancer automatiquement un devis resté sans réponse.</li><li>Trier et résumer les emails entrants.</li><li>Préparer un premier brouillon de devis à partir d'une demande.</li><li>Envoyer des rappels de rendez-vous par email ou SMS.</li><li>Rédiger des brouillons de publications pour les réseaux sociaux.</li><li>Créer des visuels et des vidéos courtes à partir d'un modèle.</li><li>Rédiger des fiches produits à partir de quelques caractéristiques.</li><li>Produire un compte rendu à partir de notes de réunion.</li></ol>"),
      ("Les précautions", "<ul><li><strong>Relisez</strong> ce que l'IA écrit avant de l'envoyer à un client, au moins au début.</li><li><strong>Limitez les données</strong> transmises aux services d'IA au strict nécessaire.</li><li><strong>Informez</strong> vos clients dans votre politique de confidentialité.</li><li><strong>Mesurez</strong> le temps gagné pour savoir si l'automatisation vaut son coût.</li></ul>"),
      ("Combien ça coûte ?", "<p>Pour une petite structure, le coût des services d'IA se compte souvent en quelques euros par mois ; l'essentiel du budget est la mise en place initiale. Je propose un diagnostic gratuit pour repérer une ou deux tâches à automatiser en priorité : voir l'<a href=\"/automatisation-ia\">automatisation IA</a>.</p>"),
    ],
  },
]
