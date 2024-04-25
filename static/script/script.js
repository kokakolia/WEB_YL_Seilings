function showImage(id) {
  const id_block = id.split("_")[0];
  let srces = [];

  im = document.getElementById(`${id_block}_1`);

  for (let i = 2; im != null; i++) {
    srces.push(im.src);
    im = document.getElementById(`${id_block}_${i.toString()}`);
  }

  const carouselImages = document.getElementById("carouselImages");

  while (carouselImages.firstChild) {
    carouselImages.removeChild(carouselImages.firstChild);
  }

  for (let i = 0; i < srces.length; i++) {
    let new_item = document.createElement("div");
    new_item.classList.add("carousel-item");

    if (i == 0) {
      new_item.classList.add("active");
    }

    let new_image = document.createElement("img");
    new_image.src = srces[i];
    new_image.classList.add("d-block");

    new_image.style.width = "600pt";
    new_image.style.height = "300pt";
    new_image.style.margin = "auto";

    new_item.appendChild(new_image);
    carouselImages.appendChild(new_item);
  }

  const modal = document.getElementById("modalWithImages");
  modal.style.display = "block";
}

function closeImage() {
  const modal = document.getElementById("modalWithImages");
  modal.style.display = "none";
}

function trackLoadPage() {
  const currentPage = window.location.href;

  let cur_option = "";

  if (currentPage == "http://127.0.0.1:8080/reviews") {
    cur_option = "option-2";
  } else if (
    currentPage == "http://127.0.0.1:8080/about" ||
    currentPage == "http://127.0.0.1:8080/"
  ) {
    cur_option = "option-1";
  } else if (currentPage == "http://127.0.0.1:8080/order") {
    cur_option = "option-3";
  }

  const referrerPage = document.referrer || "NO";
  if (referrerPage != "NO") {
    let old_option = "";

    if (
      referrerPage == "http://127.0.0.1:8080/about" ||
      referrerPage == "http://127.0.0.1:8080/"
    ) {
      old_option = "option-1";
    } else if (referrerPage == "http://127.0.0.1:8080/reviews") {
      old_option = "option-2";
    } else if (referrerPage == "http://127.0.0.1:8080/order") {
      old_option = "option-3";
    }
    const oldpage_option = document.getElementById(old_option);
    oldpage_option.classList.remove("active-option");
  }

  const curpage_option = document.getElementById(cur_option);
  curpage_option.classList.add("active-option");
}

window.onload = function () {
  trackLoadPage();
};


const colorRadios = document.querySelectorAll(".order-color-radio");
colorRadios.forEach((radio) => {
  radio.addEventListener("change", function () {
    document.querySelectorAll(".order-color-label").forEach((label) => {
      label.classList.remove("selected");
    });
    this.nextElementSibling.classList.add("selected");
  });
});


function showPrice(){
  const width = document.getElementById('order-width-input').value;
  const length = document.getElementById('order-length-input').value;
  const lamp = document.getElementById('order-lamp-input').value;

  const price = document.getElementById('order-price');
  let cost = Number(width) + Number(length) + Number(lamp);
  price.innerHTML = `Итого ${ cost }&#8381`;
  // console.log(price, price.value);
}