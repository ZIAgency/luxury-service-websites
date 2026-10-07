"""Questions voisines ajoutées à la FAQ de chaque site (SEO / GEO).

Principe (fiches ai-seo, copywriting) : la réponse tient dans la première phrase, passage de 40 à 60 mots
qui se suffit à lui-même ; on couvre les questions proches de celles déjà posées (« fan-out ») ;
aucun chiffre ni prix inventé.

`EXTRA` : questions ajoutées à la fin de la FAQ existante.
`REPLACE` : FAQ complète qui remplace l'ancienne (site pilote).
"""

REPLACE = {
    "plomberie/01-aqua-lumiere": [
        ("Combien coûte la rénovation d'une salle de bains ?",
         "Le prix dépend de la surface, des matériaux et des équipements choisis, et il ne se donne qu'après avoir vu la pièce. Vous recevez un devis détaillé poste par poste, gratuit, avec plusieurs options si vous voulez comparer. L'état des canalisations et des évacuations change le chiffrage, c'est pourquoi la visite vient d'abord."),
        ("Combien de temps durent les travaux ?",
         "Comptez deux à quatre semaines pour une salle de bains complète, et moins d'une semaine pour remplacer une baignoire par une douche. La date de début et la durée sont écrites sur le devis, et un point chaque semaine vous tient informé."),
        ("Peut-on remplacer une baignoire par une douche à l'italienne ?",
         "Oui, dans la plupart des cas. Cela dépend de la pente possible pour l'évacuation, que nous vérifions lors de la visite. Si le sol ne permet pas une douche à fleur de sol, nous proposons un receveur extra-plat."),
        ("Quelle différence entre une douche à l'italienne et un receveur extra-plat ?",
         "La douche à l'italienne est de plain-pied avec le sol : elle demande une évacuation encastrée et une étanchéité sous le carrelage. Le receveur extra-plat se pose sur le sol, avec quelques centimètres de hauteur. Il est plus simple à installer et convient quand la pente d'évacuation est insuffisante."),
        ("Que faire en cas de fuite ou de dégât des eaux ?",
         "Coupez d'abord l'arrivée d'eau au robinet d'arrêt général, puis déclarez le sinistre à votre assureur dans les cinq jours ouvrés. Appelez-nous ensuite : un plombier se déplace dans la journée à Paris Ouest et à Neuilly, localise la fuite et rédige un rapport utile pour votre assurance."),
        ("Faut-il prévenir la copropriété ?",
         "Oui, si les travaux touchent les canalisations communes ou les parties communes. Pour des travaux à l'intérieur de votre logement, sans toucher à la structure, aucune autorisation particulière n'est en général nécessaire. Nous préparons les informations pour le syndic et respectons le règlement de l'immeuble."),
        ("Puis-je fournir mes propres équipements ?",
         "Oui. Nous vérifions leur compatibilité avant la commande, puis nous les posons comme s'il s'agissait des nôtres."),
        ("Intervenez-vous en urgence ?",
         "Oui, pour une fuite ou un dégât des eaux, un plombier se déplace dans la journée à Paris Ouest et à Neuilly-sur-Seine."),
    ],
}

EXTRA = {
    # --- avocats ---
    "avocats/01-roussel-associes": [
        ("Quel avocat choisir pour un divorce ?",
         "Un avocat spécialisé en droit de la famille, qui privilégie l'accord lorsque c'est possible. Nous vous recevons pour comprendre votre situation (enfants, logement, patrimoine) puis nous vous présentons les options : consentement mutuel ou procédure contentieuse."),
        ("Mon employeur me propose une rupture conventionnelle, dois-je accepter ?",
         "Pas avant d'avoir fait vérifier les conditions. La rupture conventionnelle est un accord amiable qui ouvre en principe droit aux allocations chômage, mais son montant et sa date se négocient. Un avocat en droit du travail relit la convention avant votre signature."),
    ],
    "avocats/02-castel-avocats": [
        ("Quand faut-il rédiger un pacte d'associés ?",
         "Dès la création de la société, ou au plus tard à l'arrivée d'un nouvel associé. Il organise ce que les statuts ne couvrent pas : départ d'un associé, désaccords, répartition des décisions. Le rédiger tôt évite des conflits coûteux plus tard."),
        ("Que vérifier dans des conditions générales de vente ?",
         "L'identité du vendeur, les prix et les délais, le droit de rétractation pour les particuliers, les garanties légales, les pénalités de retard et la juridiction compétente. Des conditions adaptées à votre activité protègent aussi votre trésorerie en cas d'impayé."),
    ],
    "avocats/03-delmas-victimes": [
        ("Qu'est-ce qu'un préjudice corporel ?",
         "L'ensemble des conséquences d'un accident sur la personne : frais de santé, perte de revenus, souffrances endurées, atteinte esthétique, gêne dans la vie quotidienne. Chaque poste est évalué séparément, d'où l'importance de tous les faire reconnaître."),
        ("Quand consulter un avocat après un accident ?",
         "Le plus tôt possible, avant la consolidation de votre état, avant l'expertise médicale et avant toute offre de l'assureur. Rien ne vous oblige à signer une proposition dans l'urgence."),
    ],
    "avocats/04-leroy-defense": [
        ("Que faire si je reçois une convocation au tribunal ?",
         "Ne l'ignorez pas : contactez un avocat dès réception, convocation en main. Il vérifie les faits reprochés, la date d'audience et prépare votre défense. Ne pas vous présenter peut conduire à un jugement en votre absence."),
        ("Peut-on contester un retrait de permis ?",
         "Oui, dans certains cas, par un recours devant le tribunal administratif, avec des délais courts à respecter. Un avocat examine la procédure (contrôle, mesure de suspension) et les moyens de contestation possibles."),
    ],
    # --- bâtiment ---
    "platriers/01-morel-platrerie": [
        ("Peut-on isoler en même temps qu'on pose une cloison ou un doublage ?",
         "Oui, et c'est conseillé : les doublages isolants associent plaque de plâtre et isolant dans un seul chantier. Vous gagnez en confort thermique et acoustique sans refaire les murs deux fois."),
        ("Comment réparer une fissure dans un mur ou un plafond ?",
         "Cela dépend de son origine. Une fissure fine d'enduit se rebouche avec bande et enduit. Une fissure qui s'élargit ou traverse le mur doit d'abord être diagnostiquée. Nous venons voir avant de chiffrer."),
    ],
    "isolation/01-garnier-isolation": [
        ("Combles perdus ou combles aménagés : quelle différence pour l'isolation ?",
         "Les combles perdus, non habités, s'isolent par soufflage ou par rouleaux posés au sol, rapidement. Les combles aménagés demandent d'isoler les rampants sous la toiture, ce qui est plus long et plus technique."),
        ("Pourquoi faut-il un artisan RGE pour obtenir des aides ?",
         "Parce que la plupart des aides à la rénovation énergétique exigent que les travaux soient réalisés par une entreprise qualifiée RGE (reconnu garant de l'environnement). Sans cette qualification, vous risquez de perdre l'aide."),
    ],
    "terrassiers/01-lebrun-terrassement": [
        ("Faut-il une étude de sol avant de construire ?",
         "Oui dans de nombreuses zones : elle est obligatoire dans les secteurs exposés au retrait-gonflement des argiles, et elle détermine les fondations adaptées. Nous vous aidons à vérifier si votre terrain est concerné."),
        ("Combien de temps faut-il pour viabiliser un terrain ?",
         "Cela dépend des distances aux réseaux et des délais des gestionnaires pour les raccordements, souvent le point le plus long. Nous faisons le point sur chaque réseau dès la visite pour vous annoncer un calendrier réaliste."),
    ],
    "macons/01-maconnerie-rocher": [
        ("Quelle différence entre déclaration préalable et permis de construire ?",
         "La déclaration préalable suffit pour des travaux de faible ampleur, le permis de construire est exigé au-delà de certaines surfaces ou si le projet modifie sensiblement le bâtiment. Le seuil exact dépend de votre zone : la mairie le confirme."),
        ("Quand faut-il des fondations spécifiques ?",
         "Dès qu'on construit ou qu'on étend : leur profondeur et leur type dépendent du sol et de la charge. Une étude de sol peut être nécessaire, notamment dans les zones argileuses."),
    ],
    # --- artisanat ---
    "tapissiers/01-atelier-delorme": [
        ("Vaut-il la peine de refaire un vieux fauteuil ?",
         "Souvent oui, si la structure en bois est saine : refaire la garniture est plus raisonnable qu'un meuble neuf de qualité équivalente, et vous gardez un siège de caractère. Nous examinons l'état du bâti sur photo avant de vous conseiller."),
        ("Quel tissu choisir pour un canapé du quotidien ?",
         "Un tissu résistant à l'usure et facile d'entretien : microfibre, lin enduit ou velours de coton dense. Nous vous montrons des échantillons et vous indiquons le classement d'usure avant de choisir."),
    ],
    "cuisinistes/01-ferrer-cuisines-stores": [
        ("Comment bien choisir un store banne ?",
         "Selon l'exposition de la terrasse, la largeur de projection et la toile : une toile teintée dans la masse résiste mieux au soleil, et un coffre protège la toile quand le store est rentré. Nous mesurons sur place avant de conseiller."),
        ("Un volet roulant motorisé fonctionne-t-il en cas de coupure de courant ?",
         "La plupart disposent d'une manœuvre de secours manuelle pour le relever ou le baisser. Nous vous la montrons lors de la pose."),
    ],
    "cordonniers/01-cordonnerie-saint-clair": [
        ("Peut-on faire réparer des chaussures en daim ou en cuir clair ?",
         "Oui pour les semelles, les talons et les coutures. Pour le nettoyage et la teinture, le résultat dépend de la matière : nous vous disons franchement ce qui est réalisable avant de commencer."),
        ("Réparer ou racheter : quand une chaussure ne vaut-elle plus la peine ?",
         "Quand l'empeigne est trop usée ou déformée. Si seule la semelle est usée, une chaussure de qualité se ressemelle souvent plusieurs fois. Apportez-la, nous vous donnons un avis honnête."),
    ],
    "carrossiers/01-carrosserie-dumas": [
        ("Comment déclarer un sinistre auto ?",
         "Remplissez le constat amiable avec l'autre conducteur, puis déclarez le sinistre à votre assureur dans le délai prévu par votre contrat (souvent cinq jours ouvrés). Passez ensuite à l'atelier : nous réalisons le devis et suivons l'expertise avec vous."),
        ("Une rayure se répare-t-elle sans repeindre tout le panneau ?",
         "Souvent oui : un polissage suffit pour une rayure superficielle, une retouche locale pour une rayure plus profonde. Si la peinture est enlevée jusqu'à la tôle, le panneau est repeint. Nous vous disons ce qui est nécessaire."),
    ],
    # --- dentistes ---
    "dentistes/01-eclat-dental": [
        ("Quelle différence entre des facettes et des couronnes ?",
         "La facette recouvre la face visible de la dent, avec peu ou pas de préparation. La couronne entoure toute la dent et sert quand elle est très abîmée. Le choix dépend de l'état de la dent, que nous examinons en consultation."),
        ("Comment entretenir un sourire après un traitement esthétique ?",
         "Brossage deux fois par jour, fil ou brossettes interdentaires, et contrôle régulier chez le dentiste. Le café et le thé peuvent teinter les dents blanchies : nous vous donnons les conseils adaptés à votre traitement."),
    ],
    "dentistes/02-arcline-dental": [
        ("À quoi sert la radio 3D avant la pose d'un implant ?",
         "Elle montre le volume et la qualité de l'os en trois dimensions, ce qui permet de planifier la position exacte de l'implant et d'éviter les nerfs et les sinus. Le plan de traitement est ensuite expliqué sur écran."),
        ("Un implant peut-il être posé le jour d'une extraction ?",
         "Parfois, si l'os et la gencive le permettent. Dans d'autres cas, il faut attendre la cicatrisation. La consultation et la radio permettent de choisir la solution la plus sûre pour vous."),
    ],
    "dentistes/03-hollyfield-dental": [
        ("Les soins dentaires des enfants sont-ils pris en charge ?",
         "Oui : l'Assurance maladie rembourse les soins des enfants et propose des examens de prévention aux âges clés. Nous pratiquons le tiers payant, vous n'avez donc généralement rien à avancer sur la part remboursée."),
        ("Comment prévenir les caries chez l'enfant ?",
         "Brossage deux fois par jour avec un dentifrice fluoré adapté à l'âge, moins de boissons et d'aliments sucrés, et visites régulières. Le dentiste peut aussi poser un vernis fluoré ou protéger les sillons des molaires."),
    ],
    "dentistes/04-still-point-dental": [
        ("Peut-on être endormi pendant les soins ?",
         "Nous ne pratiquons pas d'anesthésie générale au cabinet. Nous proposons le MEOPA pour vous détendre et une anesthésie locale pour éviter la douleur. Pour des soins très longs, nous pouvons vous orienter vers un confrère équipé."),
        ("Comment gérer la peur du dentiste avant le rendez-vous ?",
         "Dites-le dès la prise de rendez-vous : nous prévoyons un créneau plus long et un déroulé adapté. Convenir d'un signal pour arrêter à tout moment aide beaucoup à retrouver le contrôle."),
    ],
    "dentistes/05-nova-smile": [
        ("Quelle différence entre gouttières et appareil fixe ?",
         "Les gouttières sont transparentes et amovibles, adaptées à de nombreux cas. L'appareil fixe est collé aux dents et reste indiqué pour les déplacements complexes. La consultation permet de trancher."),
        ("Peut-on boire du café avec des gouttières ?",
         "Retirez-les pour manger et pour boire autre chose que de l'eau, puis brossez-vous les dents avant de les remettre : cela évite taches et caries."),
    ],
    # --- ophtalmologie ---
    "ophtalmologie/01-iris-prive": [
        ("Comment savoir si mes lunettes sont bien ajustées ?",
         "Elles doivent tenir sans glisser ni serrer, avec les verres centrés devant vos pupilles. Un réglage en boutique prend quelques minutes et vaut la peine après les premières semaines d'usage."),
        ("Peut-on essayer plusieurs montures de créateurs avant de choisir ?",
         "Oui, c'est le but de l'essayage privé : vous essayez plusieurs montures et nous vous conseillons selon votre visage et votre correction."),
    ],
    "ophtalmologie/02-meridian-eye": [
        ("En quoi consiste la chirurgie de la cataracte ?",
         "Elle remplace le cristallin opacifié par un implant transparent. L'opération est rapide, se fait le plus souvent en ambulatoire, et elle est prise en charge par l'Assurance maladie lorsqu'elle est médicalement indiquée."),
        ("Quels examens faire avant une chirurgie réfractive ?",
         "Un bilan complet : mesure de la vue, de la cornée (épaisseur, forme), du fond d'œil et de la pression de l'œil. Il confirme que l'opération est possible et choisit la technique la plus adaptée."),
    ],
    "ophtalmologie/03-hawthorne-eye": [
        ("À partir de quel âge faut-il surveiller le glaucome ?",
         "Un dépistage est conseillé à partir de 40 ans, plus tôt en cas d'antécédent familial. Le glaucome évolue souvent sans symptôme : seule la mesure de la pression de l'œil et l'examen du nerf optique le détectent."),
        ("Comment se passe le renouvellement de lunettes pour un enfant ?",
         "Après examen, l'ophtalmologiste prescrit les verres adaptés. Pour un renouvellement, l'orthoptiste peut réaliser les mesures préparatoires, ce qui raccourcit l'attente."),
    ],
    "ophtalmologie/04-serene-vision": [
        ("Les écrans provoquent-ils la sécheresse oculaire ?",
         "Ils y contribuent : on cligne moins souvent devant un écran, donc le film de larmes se renouvelle moins. Des pauses régulières et des clignements volontaires aident, mais un bilan reste utile si la gêne persiste."),
        ("Quand consulter pour une sécheresse oculaire ?",
         "Dès que la gêne est quotidienne : brûlures, yeux rouges, sensation de sable ou larmoiement persistant. Un bilan identifie la cause et évite que la situation s'installe."),
    ],
    "ophtalmologie/05-vizn-lab": [
        ("Combien de temps dure un examen de dépistage de la rétine ?",
         "En général moins d'une heure, du dépistage à l'explication du résultat. Selon les examens (OCT, rétinographie), certains se font sans dilatation. Les résultats vous sont expliqués le jour même."),
        ("À quelle fréquence faire un dépistage de la rétine ?",
         "Cela dépend de votre âge et de vos facteurs de risque : diabète, antécédents familiaux, forte myopie. L'ophtalmologiste fixe le rythme adapté, souvent tous les un à deux ans."),
    ],
    # --- paysagistes ---
    "paysagistes/01-seve-pierre": [
        ("Quelle différence entre un paysagiste et un jardinier ?",
         "Le paysagiste conçoit et crée le jardin (plans, terrasses, plantations), le jardinier l'entretient au quotidien. Chez nous, les deux se rejoignent : un projet suivi de sa conception à son entretien."),
        ("Quelle terrasse choisir : bois, pierre ou composite ?",
         "Le bois a du charme et demande de l'entretien, la pierre est durable et plus coûteuse, le composite est stable et sans entretien régulier. Nous comparons selon l'exposition, l'usage et le budget."),
    ],
    "paysagistes/02-allees-vertes": [
        ("Quel est le calendrier d'entretien d'un jardin au fil des saisons ?",
         "Des tontes régulières du printemps à l'automne, la taille des haies au printemps et en fin d'été, le ramassage des feuilles à l'automne, puis un nettoyage de fin d'hiver. Nous adaptons le calendrier à votre jardin."),
        ("Peut-on arrêter ou suspendre l'entretien ?",
         "Oui, selon les conditions de votre contrat. Pour un entretien ponctuel, il n'y a pas d'engagement ; pour un contrat régulier, les conditions de résiliation sont écrites dans le devis."),
    ],
    "paysagistes/03-cime-racine": [
        ("Quels signes montrent qu'un arbre est dangereux ?",
         "Des branches mortes, un tronc fissuré ou creux, des champignons au pied, une inclinaison qui s'accentue ou des racines soulevées. Un arbre qui présente ces signes mérite un avis rapide, surtout près d'une maison ou d'une route."),
        ("Que deviennent les branches après l'élagage ?",
         "Elles sont broyées sur place ou évacuées en déchetterie, selon votre choix. Le broyat peut servir de paillage dans votre jardin. C'est précisé dans le devis."),
    ],
    "paysagistes/04-jardins-de-garrigue": [
        ("Quelles plantes choisir pour un jardin méditerranéen ?",
         "Lavande, romarin, cistes, thym, oliviers, graminées et vivaces adaptées au sec. Le bon choix dépend de l'exposition et du sol, que nous observons lors de la visite."),
        ("Le goutte-à-goutte est-il indispensable ?",
         "Il est utile les premiers étés, le temps que les racines s'installent : il arrose au pied des plantes et économise l'eau. Il peut ensuite être réduit, voire supprimé, une fois le jardin établi."),
    ],
    # --- plomberie ---
    "plomberie/02-meridian": [
        ("Comment éviter un dégât des eaux ?",
         "Repérez le robinet d'arrêt général, faites contrôler régulièrement flexibles et joints, et surveillez votre compteur en cas de doute. Un coupe-eau automatique limite les dégâts en cas de fuite."),
        ("Que faire si un robinet goutte ?",
         "C'est souvent un joint ou une cartouche à remplacer, une réparation rapide. Laissé tel quel, il peut user le robinet et alourdir la facture d'eau."),
    ],
    "plomberie/03-copperline": [
        ("Quelles adaptations rendent une salle de bains plus sûre ?",
         "Une douche de plain-pied, des barres d'appui, un siège de douche et un sol antidérapant réduisent le risque de chute. Nous adaptons selon l'autonomie de la personne."),
        ("Combien de temps dure une visite d'entretien de chaudière ?",
         "En général environ une heure, selon l'appareil : contrôle de la combustion, nettoyage, réglages et remise de l'attestation."),
    ],
    "plomberie/04-stillwater": [
        ("À quelle fréquence faut-il détartrer un chauffe-eau ?",
         "Tous les un à deux ans selon la dureté de l'eau. Un chauffe-eau entartré consomme plus et s'use plus vite."),
        ("Pourquoi la pression de ma chaudière baisse-t-elle ?",
         "Une baisse régulière peut signaler une petite fuite sur le circuit ou un vase d'expansion à contrôler. Remettez de l'eau selon la notice, et appelez-nous si cela se répète."),
    ],
    "plomberie/05-nexa": [
        ("Que contient le rapport de recherche de fuite ?",
         "La localisation précise de la fuite, la méthode utilisée, des photos et les constatations utiles à votre dossier d'assurance."),
        ("Pourquoi ma facture d'eau a-t-elle augmenté ?",
         "Une fuite invisible (chasse d'eau, canalisation enterrée ou encastrée) peut en être la cause. Le test du compteur permet de le vérifier avant d'appeler."),
    ],
    # --- serrurerie ---
    "serrurerie/01-bastion-clef": [
        ("Combien d'étoiles A2P choisir pour une serrure ?",
         "Une étoile résiste à l'effraction de base, trois étoiles offrent la plus haute résistance. Le niveau conseillé dépend de votre exposition et de votre assureur, que nous vérifions pendant l'audit."),
        ("Un coffre-fort doit-il être fixé ?",
         "Oui : un coffre scellé ou boulonné au sol ou au mur résiste mieux au vol qu'un coffre simplement posé. Nous conseillons l'emplacement et le type de fixation."),
    ],
    "serrurerie/02-keystone-lock": [
        ("Que faire si ma clé casse dans la serrure ?",
         "N'insistez pas : un morceau coincé s'extrait avec des outils adaptés, souvent sans changer le cylindre. Appelez-nous avec une photo de la porte."),
        ("Comment savoir si ma serrure est assez sûre ?",
         "Un cylindre certifié et une serrure multipoints sont de bons signes. Nous examinons la porte et vous indiquons si elle vous protège correctement."),
    ],
    "serrurerie/03-ironhaven": [
        ("Que faire si je perds une clé sécurisée ?",
         "Une clé protégée ne se copie qu'avec votre carte de propriété. Si vous la perdez, prévenez-nous : nous en commandons une nouvelle et, si besoin, nous changeons le cylindre."),
        ("Peut-on copier une clé de boîte aux lettres ?",
         "Oui, en boutique, à partir de la clé d'origine. Apportez-la avec vous : la copie se fait en quelques minutes."),
    ],
    "serrurerie/04-haven-hour": [
        ("Faut-il justifier de son identité pour une ouverture de porte ?",
         "Oui, le serrurier vérifie que vous habitez bien le logement avant d'intervenir : pièce d'identité et justificatif de domicile (facture, courrier). C'est pour votre sécurité."),
        ("Peut-on sécuriser une porte provisoirement ?",
         "Oui, par une mise en sécurité provisoire (verrou, cylindre de secours), en attendant le remplacement définitif de la serrure."),
    ],
    "serrurerie/05-aperio": [
        ("Combien de temps dure le remplacement d'un interphone en copropriété ?",
         "Après le vote en assemblée générale, l'installation prend en général quelques jours selon la taille de l'immeuble, avec un planning communiqué aux résidents."),
        ("Comment gérer les accès des prestataires (ménage, livraisons) ?",
         "Des badges Vigik, des codes temporaires ou des accès par application donnent des droits limités dans le temps, que le gestionnaire retire à tout moment."),
    ],
    # --- taxis ---
    "taxis/01-onyx-chauffeur": [
        ("Peut-on réserver un chauffeur à l'heure ?",
         "Oui : la mise à disposition garde le chauffeur pour plusieurs trajets et rendez-vous dans la journée, avec un tarif annoncé à la réservation."),
        ("Les véhicules conviennent-ils aux bagages ?",
         "Berlines et vans accueillent plusieurs valises. Indiquez le nombre de bagages à la réservation pour choisir le bon véhicule."),
    ],
    "taxis/02-vector-taxi": [
        ("Peut-on réserver un taxi pour plusieurs trajets dans la journée ?",
         "Oui, nous planifions les trajets avec des horaires convenus à l'avance, et un prix annoncé pour chacun."),
        ("Les animaux sont-ils acceptés ?",
         "Les chiens guides d'aveugle sont toujours acceptés. Pour les autres animaux, prévenez-nous à la réservation : le chauffeur confirme selon le véhicule."),
    ],
    "taxis/03-checker-cab": [
        ("Qu'est-ce qu'une prescription médicale de transport ?",
         "Un document rempli par votre médecin, qui précise le motif et le mode de transport. Il est nécessaire pour que le trajet puisse être pris en charge par l'Assurance maladie."),
        ("Faut-il avancer les frais d'un transport médical ?",
         "Le plus souvent non : le tiers payant permet que la part prise en charge soit réglée directement, selon votre situation."),
    ],
    "taxis/04-lumen-ride": [
        ("Comment réserver pour une personne qui n'utilise pas internet ?",
         "Par téléphone : nous notons l'adresse, l'heure du rendez-vous et les besoins particuliers, et nous prévenons la famille si vous le souhaitez."),
        ("Les longs trajets sont-ils fatigants pour une personne âgée ?",
         "Nous prévoyons des pauses à la demande et une conduite souple. Précisez vos besoins à la réservation."),
    ],
    "taxis/05-pulse-taxi": [
        ("Comment suivre l'arrivée du taxi ?",
         "Vous recevez l'heure d'arrivée par SMS, puis le chauffeur vous prévient en arrivant."),
        ("Peut-on réserver un taxi pour une soirée ou un événement ?",
         "Oui, nous pouvons planifier l'aller et le retour avec un horaire convenu à l'avance."),
    ],
}
