
const map = L.map("map").setView(
    [-3.1190, -60.0217], // Manaus
    13
);

L.tileLayer(

    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",

    {

        attribution:
        "&copy; OpenStreetMap Contributors",

        maxZoom:19

    }

).addTo(map);

const iconeVermelho = L.icon({
    iconUrl: 'img/marker-vermelho.png', // caminho da imagem
    iconSize: [25, 41],                 // largura, altura
    iconAnchor: [12, 41],               // ponto que toca o mapa
    popupAnchor: [1, -34],              // posição do popup
    shadowUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png',
    shadowSize: [41, 41]
});

fetch("dados.json")
.then(response => response.json())
.then(dados => {
   
    const origem = L.marker(dados.origem)
        .addTo(map)
        .bindPopup("Origem");

    const destino = L.marker(dados.destino)
        .addTo(map)
        .bindPopup("Destino");

    dados.caminho[0].nos_Filhos.forEach(ponto => {
        console.log('Pai: '+dados.caminho[0].no_Pai+'  filho:'+ponto)
        let pontos = [dados.caminho[0].no_Pai, ponto]

        L.polyline(pontos, {
                color: 'blue',
                weight: 5,
                opacity: 0.8
            }).addTo(map);

    });
        
    map.fitBounds(rota.getBounds());

    

});



