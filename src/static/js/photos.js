document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.querySelector(".carousel-images");
    const images = document.querySelectorAll(".carousel-images img");
    const totalImages = images.length;
    let currentIndex = 0;

    function moveCarousel() {
        // Calcula el ancho total de cada imagen
        const imageWidth = images[0].clientWidth;
        // Mueve el carrusel hacia la izquierda
        currentIndex++;
        if (currentIndex >= totalImages) {
            currentIndex = 0; // Regresa al inicio cuando termine
        }
        carousel.style.transform = `translateX(-${currentIndex * imageWidth}px)`;
    }

    // Configura el temporizador para moverse cada 3 segundos
    setInterval(moveCarousel, 3000);
});
