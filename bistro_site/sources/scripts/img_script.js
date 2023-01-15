let wrapper = document.querySelector('.input_field-img-icon');

function download(input){
    let file = input.files[0];
    let reader = new FileReader();
    reader.readAsDataURL(file);

    reader.onload = function() {
        wrapper.src = reader.result;
        wrapper.className = 'loaded_img'
    }
}
