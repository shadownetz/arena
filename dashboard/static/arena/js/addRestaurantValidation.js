$(function(){
    // Enable flatpickr time for field
    $('.time-picker').flatpickr({
        noCalendar: true,
        enableTime: true,
        dateFormat: 'H:i'
    });

    // Prevent auto-form submittion and validate add event fields
    $('.js-add-event-form').click(formCheck);

    $('#id_owner').on('keyup', validateForm);
    $('#id_name').on('keyup', validateForm);
    $('#id_category').on('change', validateForm);
    $('#id_mail').on('keyup', validateForm);
    $('#id_website').on('keyup', validateForm);
    $('#id_phone').on('keyup', validateForm);
    $('#id_address').on('keyup', validateForm);
    $('#id_country').on('change', validateForm);
    $('#id_state').on('change', validateForm);
    $('#id_image_rep').on('change', validateForm);
    $('#id_open_time').on('change', validateForm);
    $('#id_close_time').on('change', validateForm);
    $('#id_date_history').on('change', validateForm);

    // display filename
    $('#id_image_rep').change(function(e){
        let filename = e.target.files[0].name;
        setTimeout(function(){
            $('.custom-file-label').html(filename);
        }, 500);
    })
});

// store our fields values
let owner_input = $('#id_owner');
let item_name = $('#id_name');
let item_category = $('#id_category');
let event_mail = $('#id_mail');
let item_ingredients = $('#id_address');
let event_website = $('#id_website');
let event_phone = $('#id_phone');
let item_country = $('#id_country');
let item_state = $('#id_state');
let item_image = $('#id_image_rep')
let open_time = $('#id_open_time');
let close_time = $('#id_close_time');
let event_history = $('#id_date_history');
let error_status = 0;

function validateEmail(email) {
    /**
     * Function to validate email address
     * @type {RegExp}
     */
    let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

function formCheck(event){
    event.preventDefault(); // prevent form submission
    validateForm();

    if(error_status === 0){
        $('#addEventForm').trigger('submit');
    }
}

function validateForm(){
    error_status = 0;

    if(owner_input.val() == ''){
        owner_input.addClass('is-invalid');
        ++error_status;
    }else{
        owner_input.removeClass('is-invalid');
        owner_input.addClass('is-valid');
    }
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
    let email_val = event_mail.val();
    let email_status = validateEmail(email_val);
    if(email_val == '' || !email_status){
        event_mail.addClass('is-invalid');
        ++error_status;
    }else{
        event_mail.removeClass('is-invalid');
        event_mail.addClass('is-valid');
    }
    if(item_ingredients.val() == ''){
        item_ingredients.addClass('is-invalid');
        ++error_status;
    }else{
        item_ingredients.removeClass('is-invalid');
        item_ingredients.addClass('is-valid');
    }
    if(event_website.val() == ''){
        event_website.addClass('is-invalid');
        ++error_status;
    }else{
        event_website.removeClass('is-invalid');
        event_website.addClass('is-valid');
    }
    if(event_phone.val() == ''){
        event_phone.addClass('is-invalid');
        ++error_status;
    }else{
        event_phone.removeClass('is-invalid');
        event_phone.addClass('is-valid');
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
    if(open_time.val() == ''){
        open_time.addClass('is-invalid');
        ++error_status;
    }else{
        open_time.removeClass('is-invalid');
        open_time.addClass('is-valid');
    }
    if(close_time.val() == ''){
        close_time.addClass('is-invalid');
        ++error_status;
    }else{
        close_time.removeClass('is-invalid');
        close_time.addClass('is-valid');
    }
    if(event_history.val() == ''){
        event_history.addClass('is-invalid');
        ++error_status;
    }else{
        event_history.removeClass('is-invalid');
        event_history.addClass('is-valid');
    }

}