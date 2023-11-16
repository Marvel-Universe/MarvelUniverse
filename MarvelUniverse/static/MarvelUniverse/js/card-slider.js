const carousels = document.querySelectorAll(".carousel");
for (i = 0; i < carousels.length; i++) {
    const carousel = document.querySelector(`#id${i+1} .carousel`)

    const arrowBtns = document.querySelectorAll(`#id${i+1} i`)
    const fisrtCardWidth = carousel.querySelector(".card").offsetWidth;
    const carouselChildrens = [...carousel.children];

    let isDragging = false;
    let cardPerView = Math.round(carousel.offsetWidth / fisrtCardWidth)

    carouselChildrens.slice(-cardPerView).reverse().forEach(card => {
        carousel.insertAdjacentHTML("afterbegin", card.outerHTML)
    })

    carouselChildrens.slice(0, cardPerView).forEach(card => {
        carousel.insertAdjacentHTML("beforeend", card.outerHTML)
    })

    arrowBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            carousel.scrollLeft += btn.id === "left" ? -fisrtCardWidth * cardPerView : fisrtCardWidth * cardPerView;
        })
    })

    const dragStart = (e) => {
        isDragging = true;
        carousel.classList.add("dragging");
        // Records the initial cursor and scroll position of the carousel
        startX = e.pageX
        startScrollLeft = carousel.scrollLeft
    }

    const dragging = (e) => {
        if (!isDragging) return;
        carousel.scrollLeft = startScrollLeft
            - (e.pageX - startX);
        console.log(e.pageX)
    }

    const dragStop = () => {
        isDragging = false;
        carousel.classList.remove("dragging")
    }

    carousel.addEventListener("mousedown", dragStart);
    carousel.addEventListener("mousemove", dragging);
    document.addEventListener("mouseup", dragStop);
}
