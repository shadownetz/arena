$(function(){

    // Prevent auto-form submission and validate add item fields
    $('.js-add-food-drink-form').click(formCheck);

    $('#id_name').on('keyup', validateForm);
    $('#id_category').on('change', validateForm);
    $('#id_ingredients').on('keyup', validateForm);
    $('#id_assoc_country').on('change', validateForm);
    $('#id_assoc_states').on('change', validateForm);
    $('#id_image_rep').on('change', validateForm);

    // display filename
    $('#id_image_rep').change(function(e){
        let filename = e.target.files[0].name;
        setTimeout(function(){
            $('.custom-file-label').html(filename);
        }, 500);
    })
});

// store our fields values
let item_name = $('#id_name');
let item_category = $('#id_category');
let item_ingredients = $('#id_ingredients');
let item_country = $('#id_assoc_country');
let item_state = $('#id_assoc_states');
let item_image = $('#id_image_rep');
let error_status = 0;

function formCheck(event){
    event.preventDefault(); // prevent form submission
    let form_id = $('#addFoodDrinkForm');
    validateForm();

    if(error_status === 0){
            form_id.trigger('submit');
    }
}

function validateForm(){
    error_status = 0;

    if(item_name.val() == ''){
        item_name.addClass('is-invalid');
        ++error_status;
    }else{
        item_name.removeClass('is-invalid');
        item_name.addClass('is-valid');
    }
    let child = item_category.next();
    let child_desc1 = child.contents();
    let child_desc2 = child_desc1.contents();
    if(item_category.val() == ''){
        child_desc2.css('border-color', '#dc3545');
        ++error_status;
    }else{
        child_desc2.css('border-color', '#28a745');
    }
    if(item_ingredients.val() == ''){
        item_ingredients.addClass('is-invalid');
        ++error_status;
    }else{
        item_ingredients.removeClass('is-invalid');
        item_ingredients.addClass('is-valid');
    }
    let child_one = item_country.next();
    let child_one_desc1 = child_one.contents();
    let child_one_desc2 = child_one_desc1.contents();
    if(item_country.val() == ''){
        child_one_desc2.css('border-color', '#dc3545');
        ++error_status;
    }else{
        child_one_desc2.css('border-color', '#28a745');
    }
    let child_two = item_state.next();
    let child_two_desc1 = child_two.contents();
    let child_two_desc2 = child_two_desc1.contents();
    if(item_state.val() == ''){
        child_two_desc2.css('border-color', '#dc3545');
        ++error_status;
    }else{
        child_two_desc2.css('border-color', '#28a745');
    }
    if(item_image.val() == ''){
        item_image.addClass('is-invalid');
        ++error_status;
    }else{
        item_image.removeClass('is-invalid');
        item_image.addClass('is-valid');
    }
}