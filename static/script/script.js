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

    new_image.style.width = "75vw";
    new_image.style.height = "80vh";
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
    if (old_option != ''){
      const oldpage_option = document.getElementById(old_option);
      oldpage_option.classList.remove("active-option");
    }
    
  }
  if (cur_option != ''){
    const curpage_option = document.getElementById(cur_option);
    curpage_option.classList.add("active-option");
    console.log(3, curpage_option)
  }
  
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
  if (cost){
    console.log(cost, cost!= NaN, typeof(cost))
    price.innerHTML = `Итого ${ cost }&#8381`;
  }
}

function redirect(ref,  arg=null){
  if (arg){
    window.location = `${ref}/${arg}`
  }
  else{
    window.location = ref;
  }
}
images_to_delete = []
function deleteImage(){

  block = document.querySelector('.change-review-form .carousel-inner .active');
  if (block){
    block.style.display = 'none';
  block.classList.remove('carousel-item');
  block.classList.remove('active')
  img = block.querySelector('img').src;
  images_to_delete.push(img);


  next_block_list = document.querySelectorAll('.change-review-form .carousel-inner div');
  for (let i = 0;i < next_block_list.length;i++){
    cur_block = next_block_list[i];
    if (cur_block.style.display != 'none'){
      cur_block.classList.add('active');
      break;
    }
  }
  console.log(img, cur_block)
  }
  
  // console.log(next_block_list);

}

function postData(){
  const formData = new FormData(document.getElementById("form-to-change"));
  const carouselData = [];
  const els = document.getElementsByClassName("carousel-item");
  for (let i = 0; i < els.length; i++){
    el = els[i];
    srcs = el.querySelector('img').src;
    srcs = srcs.slice(srcs.indexOf('static/users_img/'));
    carouselData.push(srcs);
  }
  console.log(carouselData);
  json = JSON.stringify(carouselData)
  console.log(json)
  formData.append('carouselData', JSON.stringify(carouselData));
  
  fetch('', {
    method: 'POST',
    body: formData
  }).then(response => response.text())
  .then(html => {
      document.body.innerHTML = html;
  })
}