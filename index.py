<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Juego de Cartas - Batalla</title>
    <style>
        body { font-family: Arial, background: #222; color: white; text-align: center; }
        .cartas-container { display: flex; justify-content: center; margin: 20px; }
        .carta { background: #333; border: 2px solid #555; border-radius: 10px; padding: 10px; margin: 10px; width: 150px; }
        img { width: 100px; height: 100px; border-radius: 8px; }
        .ganador { font-size: 24px; margin-top: 20px; color: #0f0; }
        button { padding: 10px 20px; font-size: 18px; margin: 20px; }
    </style>
</head>
<body>

<h1>Juego de Cartas</h1>
<button onclick="iniciarJuego()">Iniciar Partida</button>
<div class="cartas-container">
    <div id="jugador"></div>
    <div id="vs" style="font-size: 40px; margin: 50px;">VS</div>
    <div id="cpu"></div>
</div>
<div class="ganador" id="resultado"></div>
<button onclick="siguienteRonda()">Siguiente Ronda</button>

<script>
const cartas = [
    {nombre: "John Cena", ataque: 90, defensa: 80, imagen: "https://www.kindpng.com/picc/m/36-369716_john-cena-clipart-animated-john-cena-cartoon-png.png"},
    {nombre: "Dr. Simi", ataque: 70, defensa: 95, imagen: "https://cdn.drsimi.com.mx/assets/img/drsimi/slider2.png"},
    {nombre: "La Roca", ataque: 95, defensa: 70, imagen: "https://upload.wikimedia.org/wikipedia/en/e/e0/Dwayne_Johnson_as_the_Rock.png"},
    {nombre: "Chabelo", ataque: 50, defensa: 100, imagen: "https://i.imgur.com/fqhNArU.png"},
    {nombre: "Shrek", ataque: 85, defensa: 90, imagen: "https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.png"},
    {nombre: "Goku", ataque: 100, defensa: 70, imagen: "https://i.imgur.com/9n1cLeT.png"},
    {nombre: "Vegeta", ataque: 95, defensa: 75, imagen: "https://i.imgur.com/Gm7RDEm.png"},
    {nombre: "Spiderman", ataque: 80, defensa: 85, imagen: "https://i.imgur.com/Vxg7VEz.png"},
    {nombre: "Batman", ataque: 70, defensa: 90, imagen: "https://i.imgur.com/W7J5pJz.png"},
    {nombre: "Deadpool", ataque: 85, defensa: 80, imagen: "https://i.imgur.com/nUI2NEO.png"},
    {nombre: "El Santo", ataque: 88, defensa: 85, imagen: "https://i.imgur.com/TC55to4.png"},
    {nombre: "Godzilla", ataque: 98, defensa: 95, imagen: "https://i.imgur.com/7WYlxAl.png"},
    {nombre: "Pikachu", ataque: 75, defensa: 80, imagen: "https://i.imgur.com/b7U7fxr.png"},
    {nombre: "Homero Simpson", ataque: 65, defensa: 85, imagen: "https://i.imgur.com/E3CBnpU.png"},
    {nombre: "Iron Man", ataque: 90, defensa: 85, imagen: "https://i.imgur.com/73hJKMY.png"},
    {nombre: "Capitán América", ataque: 80, defensa: 95, imagen: "https://i.imgur.com/7NSzrju.png"},
    {nombre: "Mario Bros", ataque: 78, defensa: 82, imagen: "https://i.imgur.com/q5We9hP.png"},
    {nombre: "Bowser", ataque: 92, defensa: 88, imagen: "https://i.imgur.com/5WgKwZD.png"},
    {nombre: "Messi", ataque: 77, defensa: 79, imagen: "https://i.imgur.com/BCz5OZF.png"},
    {nombre: "Chapulín Colorado", ataque: 70, defensa: 88, imagen: "https://i.imgur.com/bivbOtD.png"}
];

let mazoJugador = [], mazoCPU = [], cartaJugador, cartaCPU;

function iniciarJuego() {
    const mazo = [...cartas].sort(() => 0.5 - Math.random());
    mazoJugador = mazo.slice(0, 5);
    mazoCPU = mazo.slice(5, 10);
    document.getElementById("resultado").innerText = "¡Partida iniciada!";
    mostrarCartas();
}

function mostrarCartas() {
    document.getElementById("jugador").innerHTML = `<h3>Jugador (${mazoJugador.length} cartas)</h3>` + 
        (mazoJugador[0] ? generarCartaHTML(mazoJugador[0]) : "Sin cartas");
    document.getElementById("cpu").innerHTML = `<h3>CPU (${mazoCPU.length} cartas)</h3>` + 
        (mazoCPU[0] ? generarCartaHTML(mazoCPU[0]) : "Sin cartas");
}

function generarCartaHTML(carta) {
    return `<div class='carta'>
        <img src="${carta.imagen}" alt="${carta.nombre}">
        <h4>${carta.nombre}</h4>
        <p>Ataque: ${carta.ataque}</p>
        <p>Defensa: ${carta.defensa}</p>
    </div>`;
}

function siguienteRonda() {
    if (mazoJugador.length === 0 || mazoCPU.length === 0) {
        document.getElementById("resultado").innerText = mazoJugador.length === 0 ? "¡CPU gana!" : "¡Jugador gana!";
        return;
    }
    cartaJugador = mazoJugador.shift();
    cartaCPU = mazoCPU.shift();

    let resultado = "";
    if (cartaJugador.ataque > cartaCPU.defensa) {
        resultado = `¡${cartaJugador.nombre} gana!`;
    } else if (cartaCPU.ataque > cartaJugador.defensa) {
        resultado = `¡${cartaCPU.nombre} gana!`;
    } else {
        resultado = "¡Empate! Ambas cartas eliminadas.";
    }

    if (cartaJugador.ataque > cartaCPU.defensa) {
        // jugador gana, cpu pierde carta
    } else if (cartaCPU.ataque > cartaJugador.defensa) {
        // cpu gana, jugador pierde carta
    } // si es empate ambas eliminadas, ya están fuera del mazo

    document.getElementById("resultado").innerText = resultado;
    mostrarCartas();
    if (mazoJugador.length === 0 || mazoCPU.length === 0) {
        document.getElementById("resultado").innerText += mazoJugador.length === 0 ? " ¡CPU gana la partida!" : " ¡Jugador gana la partida!";
    }
}
</script>

</body>
</html>
