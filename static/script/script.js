function showImage(id) {

    const id_block = id.split('_')[0];
    let srces = []

    im = document.getElementById(`${id_block}_1`);

    for (let i = 2;im != null; i++){
        srces.push(im.src);
        im = document.getElementById(`${id_block}_${i.toString()}`)
    }

    const carouselImages = document.getElementById("carouselImages");

    while (carouselImages.firstChild) {
        carouselImages.removeChild(carouselImages.firstChild);
    }

    for (let i = 0; i < srces.length; i++) {

        let new_item = document.createElement("div");
        new_item.classList.add("carousel-item");

        if (i == 0){
            new_item.classList.add("active");
        }

        let new_image = document.createElement("img");
        new_image.src = srces[i];
        new_image.classList.add("d-block");


        new_image.style.width = "700pt";
        new_image.style.height = "400pt";

        new_item.appendChild(new_image);
        carouselImages.appendChild(new_item);

    }

    const modal = document.getElementById('modalWithImages');
    modal.style.display = 'block';

}



function closeImage() {

    const modal = document.getElementById('modalWithImages');
    modal.style.display = 'none';
    
}