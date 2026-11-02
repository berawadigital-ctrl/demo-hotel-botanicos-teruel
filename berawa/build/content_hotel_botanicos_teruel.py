# Contenido de la demo Gran Hotel Botánicos (Teruel) (es/en/fr/de). Hechos de granhotelbotanicos.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitaciones con terraza, superior y standard','Habitación plus e individual'],'en':['Rooms with terrace, superior and standard','Plus and single rooms'],'fr':['Chambres avec terrasse, supérieure et standard','Chambres plus et individuelle'],'de':['Zimmer mit Terrasse, Superior und Standard','Plus- und Einzelzimmer']}
RD={
'es':['Para 2 personas, de 14 a 17 m², con cama de matrimonio o dos individuales. Las de terraza y las superiores miran a la Vega del Turia.','La plus es la más amplia: 25 m², hasta 4 personas con sofá cama. La individual, de 13 m², da al patio interior.'],
'en':['For 2 people, 14 to 17 m², with a double bed or two singles. Terrace and superior rooms overlook the Vega del Turia.','The plus is the largest: 25 m², up to 4 people with a sofa bed. The single, 13 m², faces the inner courtyard.'],
'fr':['Pour 2 personnes, de 14 à 17 m², avec lit double ou deux lits simples. Les chambres avec terrasse et supérieures donnent sur la Vega del Turia.','La plus est la plus grande : 25 m², jusqu’à 4 personnes avec canapé-lit. L’individuelle, de 13 m², donne sur le patio intérieur.'],
'de':['Für 2 Personen, 14 bis 17 m², mit Doppelbett oder zwei Einzelbetten. Terrassen- und Superior-Zimmer blicken auf die Vega del Turia.','Das Plus-Zimmer ist das größte: 25 m², bis zu 4 Personen mit Schlafsofa. Das Einzelzimmer mit 13 m² geht zum Innenhof.']}
ART={
'hero':('hills',7711,['#1e2a24','#9a8a4e','#e9e4c8','#53645a','#34433b','#151d19']),
'intro':('columns',7712,['#eef0ea','#f9faf6','#4e5e2e','#55615a','#232b27']),
'r1':('arches',7721,['#e9ece4','#c9c27e','#4e5e2e','#55615a','#232b27']),
'r2':('hills',7722,['#1e2a24','#a7964f','#ede8cc','#5e6f64','#3a4a41','#172019']),
'g1':('waves',7731,['#1e2a24','#9a8a4e','#e9e4c8','#53645a','#34433b','#151d19']),
'g2':('skyline',7732,['#eef0ea','#f9faf6','#4e5e2e','#55615a','#232b27']),
'g3':('hills',7733,['#e4e7de','#e4dfc2','#c9c27e','#8a8f86','#62675f','#40443e']),
'g4':('columns',7734,['#1e2a24','#a7964f','#ede8cc','#5e6f64','#3a4a41','#172019'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Gran Hotel Botánicos · Hotel en el centro de Teruel con parking propio',see_rooms='Ver habitaciones',hero_k='Teruel · Camino de la Estación, 27',hero_t='Teruel a pie, con parking propio',hero_s='En pleno centro, junto al Parque de la Escalinata, con salida peatonal directa al casco histórico.',
 intro_t='Descubre Teruel a pie',intro_p1='Desde la quinta planta sales directamente al casco histórico: en pocos minutos llegas a la Plaza del Torico, la Catedral de Santa María de Mediavilla, el Mausoleo de los Amantes y las torres mudéjares.',
 intro_p2='Parking privado exclusivo para huéspedes, con acceso directo al hotel y a las habitaciones, para olvidarte de buscar aparcamiento en el casco antiguo.',
 stats=['Centro de Teruel','Parking privado','Desayuno buffet','Mirador de la Vega'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con wifi, climatización, minibar, hervidor de agua, televisión y caja fuerte.',
 svcs=['Parking privado con acceso directo a las habitaciones','Desayuno buffet','Room service de 08:00 a 11:00 y de 19:00 a 22:00','Lobby bar y Mirador de la Vega','Bike Zone con vigilancia 24 h','Salón de eventos y lavandería'],
 loc_p='Camino de la Estación, 27 · 44001 Teruel. Teléfono: 978 623 957. Correo: reservas@granhotelbotanicos.com.',
 chips=['¿Tenéis parking?','¿A qué hora es el desayuno?','¿Qué habitaciones tenéis?','¿Cómo reservo?']),
'en':dict(title='Gran Hotel Botánicos · Hotel in central Teruel with its own parking',see_rooms='See rooms',hero_k='Teruel · Camino de la Estación, 27',hero_t='Teruel on foot, with private parking',hero_s='Right in the centre, next to the Escalinata park, with a direct pedestrian exit to the old town.',
 intro_t='Discover Teruel on foot',intro_p1='From the fifth floor you step straight into the old town: within minutes you reach the Plaza del Torico, Santa María de Mediavilla Cathedral, the Mausoleum of the Lovers and the Mudéjar towers.',
 intro_p2='Private parking exclusively for guests, with direct access to the hotel and rooms, so you can forget about finding a space in the old town.',
 stats=['Central Teruel','Private parking','Buffet breakfast','Vega viewpoint'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with wifi, air conditioning, minibar, kettle, television and safe.',
 svcs=['Private parking with direct access to rooms','Buffet breakfast','Room service 08:00–11:00 and 19:00–22:00','Lobby bar and Vega viewpoint','Bike Zone with 24 h surveillance','Event room and laundry'],
 loc_p='Camino de la Estación, 27 · 44001 Teruel. Phone: +34 978 623 957. Email: reservas@granhotelbotanicos.com.',
 chips=['Do you have parking?','What time is breakfast?','Which rooms do you have?','How do I book?']),
'fr':dict(title='Gran Hotel Botánicos · Hôtel au centre de Teruel avec parking privé',see_rooms='Voir les chambres',hero_k='Teruel · Camino de la Estación, 27',hero_t='Teruel à pied, avec parking privé',hero_s='En plein centre, à côté du parc de l’Escalinata, avec une sortie piétonne directe vers la vieille ville.',
 intro_t='Découvrir Teruel à pied',intro_p1='Depuis le cinquième étage, vous sortez directement dans la vieille ville : en quelques minutes, Plaza del Torico, cathédrale Santa María de Mediavilla, mausolée des Amants et tours mudéjares.',
 intro_p2='Parking privé réservé aux clients, avec accès direct à l’hôtel et aux chambres, pour oublier la recherche d’une place dans la vieille ville.',
 stats=['Centre de Teruel','Parking privé','Petit-déjeuner buffet','Belvédère de la Vega'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec wifi, climatisation, minibar, bouilloire, télévision et coffre-fort.',
 svcs=['Parking privé avec accès direct aux chambres','Petit-déjeuner buffet','Room service de 08:00 à 11:00 et de 19:00 à 22:00','Lobby bar et belvédère de la Vega','Bike Zone surveillée 24 h/24','Salle d’événements et blanchisserie'],
 loc_p='Camino de la Estación, 27 · 44001 Teruel. Téléphone : +34 978 623 957. E-mail : reservas@granhotelbotanicos.com.',
 chips=['Avez-vous un parking ?','À quelle heure est le petit-déjeuner ?','Quelles chambres avez-vous ?','Comment réserver ?']),
'de':dict(title='Gran Hotel Botánicos · Hotel im Zentrum von Teruel mit eigenem Parkplatz',see_rooms='Zimmer ansehen',hero_k='Teruel · Camino de la Estación, 27',hero_t='Teruel zu Fuß, mit eigenem Parkplatz',hero_s='Mitten im Zentrum, neben dem Escalinata-Park, mit direktem Fußgängerausgang zur Altstadt.',
 intro_t='Teruel zu Fuß entdecken',intro_p1='Vom fünften Stock gelangen Sie direkt in die Altstadt: in wenigen Minuten zur Plaza del Torico, zur Kathedrale Santa María de Mediavilla, zum Mausoleum der Liebenden und zu den Mudéjar-Türmen.',
 intro_p2='Privatparkplatz nur für Gäste, mit direktem Zugang zum Hotel und zu den Zimmern – keine Parkplatzsuche in der Altstadt.',
 stats=['Zentrum von Teruel','Privatparkplatz','Frühstücksbuffet','Aussichtspunkt Vega'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit WLAN, Klimaanlage, Minibar, Wasserkocher, Fernseher und Safe.',
 svcs=['Privatparkplatz mit direktem Zugang zu den Zimmern','Frühstücksbuffet','Zimmerservice 08:00–11:00 und 19:00–22:00 Uhr','Lobbybar und Aussichtspunkt Vega','Bike Zone mit 24-h-Überwachung','Veranstaltungssaal und Wäscherei'],
 loc_p='Camino de la Estación, 27 · 44001 Teruel. Telefon: +34 978 623 957. E-Mail: reservas@granhotelbotanicos.com.',
 chips=['Gibt es einen Parkplatz?','Wann gibt es Frühstück?','Welche Zimmer gibt es?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://hotel.granhotelbotanicos.com/'
BOOK=dict(mode='engine',url=dict(es=R,en=R,fr=R,de=R))
D=dict(name='Gran Hotel Botánicos',ac='#1e2a24',ac2='#4e5e2e',ac2_a11y='#404d25',book=BOOK,around=[],foot=FOOT,
 address='Camino de la Estación, 27 · 44001 Teruel',phones=['+34 978 623 957'],emails=['reservas@granhotelbotanicos.com'],maps='Gran Hotel Botánicos, Camino de la Estación 27, 44001 Teruel',t=T)
META=dict(repo='demo-hotel-botanicos-teruel',name='Gran Hotel Botánicos',legal_name='GRAN HOTEL BOTANICOS S.L., NIF B70916259 (aviso legal de su web)',registry_ids=['B70916259'],
 url='https://granhotelbotanicos.com/',domain='granhotelbotanicos.com',municipality='Teruel',province='Teruel',sector='hotel en el centro de Teruel con parking propio',
 read_at='2026-11-02T09:16:00+01:00',created_at='2026-11-02T09:15:00+01:00',built_at='2026-11-02T09:30:00+01:00',audit_date='2026-11-02T09:16:00+01:00',
 rating=dict(value=4.5,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Gran+Hotel+Bot%C3%A1nicos/@40.3417367,-1.1097392,17z'),
 book=dict(mode='engine',url=R,note='motor propio que carga su web (init_booking.js de hotel.granhotelbotanicos.com, boton RESERVAR): https://hotel.granhotelbotanicos.com/, HTTP 200 y muestra «Contrata online» con fechas (02/11/2026 09:18). Mismo enlace en los 4 idiomas.'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Tenéis parking?','K03'),('¿A qué hora es el desayuno?','K04'),('¿A qué hora es la entrada?','K05'),('¿Admitís mascotas?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay servicio de habitaciones?','K09'),('¿Qué ver en Teruel?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Tenéis cunas?','K12'),('¿Vengo en bici, dónde la dejo?','K13'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Do you have parking?','K03'),('What time is breakfast?','K04'),('What time is check-in?','K05'),('Do you allow pets?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there room service?','K09'),('What to see in Teruel?','K10'),('What is your phone number?','K11'),('Do you have cots?','K12'),('Where can I leave my bike?','K13'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Avez-vous un parking ?','K03'),('À quelle heure est le petit-déjeuner ?','K04'),('À quelle heure est l’arrivée ?','K05'),('Acceptez-vous les animaux ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il un room service ?','K09'),('Que voir à Teruel ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Avez-vous des lits bébé ?','K12'),('Où laisser mon vélo ?','K13'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es einen Parkplatz?','K03'),('Wann gibt es Frühstück?','K04'),('Wann ist der Check-in?','K05'),('Sind Haustiere erlaubt?','K06'),('Wo liegt das Hotel?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es Zimmerservice?','K09'),('Was kann man in Teruel besichtigen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Haben Sie Kinderbetten?','K12'),('Wo kann ich mein Fahrrad lassen?','K13'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
