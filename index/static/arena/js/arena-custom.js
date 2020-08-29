$(function(){

    function validateEmail(email) {
        /**
         * Function to validate email address
         * @type {RegExp}
         */
        let re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(String(email).toLowerCase());
    }

    // Function to show modal when login is clicked
    function preventLinkClick(event){
        event.preventDefault();
        $("#arena-account").modal();
    }

    $('#arena-acc').click(preventLinkClick);
    $('#arena-acc-m').click(preventLinkClick);

    // insert new element to display username validation message
    $('#user').before("<span id='user-msg'></span>");

    // show modal when page loads
    // $("#arena-account").modal("show");


    // check if username exists or not
    $('#user').change(function(){
        let username = $(this).val();
        let userblock = $('#user-msg');

        $.ajax({
            url: 'ajax/validate_username',
            data:{
                'username':username
            },
            dataType: 'json',
            success: function(data){
                if(data.is_taken){
                    $('#arena-signup #user3 .err-msg').text("Username already exists");
                    $('#arena-signup #user3 .err-msg').show('slow');
                }else{
                    $('#arena-signup #user3 .err-msg').hide('slow');
                }
            }
        });
    });

    // check if email is valid or not
    $('#id_email').change(function(){
        let email_err_block = $('#arena-signup #id_email4 .err-msg');
        let content = $('#id_email').val();
        let status = validateEmail(content);
        if(!status){
            email_err_block.html("Invalid email format<br>Email should be in the format mail@example.com");
            email_err_block.show('slow');
        }else{
            email_err_block.hide('slow');
        }
    });



    // Validate Sign Up Form
    $('#arena-submit').click(function(event){
        event.preventDefault();
        let first_name = $('#id_first_name').val(); let fname_err = $('#arena-signup #id_first_name1').find('.err-msg');
        let last_name = $('#id_last_name').val();   let lname_err = $('#arena-signup #id_last_name2 .err-msg');
        let user_name = $('#user').val();           let user_err = $('#arena-signup #user3 .err-msg');
        let email_address = $('#id_email').val();   let email_err = $('#arena-signup #id_email4 .err-msg');
        let password1 = $('#id_password').val();    let pass_err = $('#arena-signup #id_password5 .err-msg');
        let password2 = $('#id_password2').val();   let repass_err = $('#arena-signup #id_password26 .err-msg');
        let error_count = 0;

        if((first_name == '') || (first_name.length <= 0)){
            error_count += 1;
            fname_err.text("This Field cannot be blank");
            fname_err.show('slow');
        }else{
            fname_err.hide('slow');
        }
        if((last_name == '') || (last_name.length <= 0)){
            error_count += 1;
            lname_err.text("This Field cannot be blank");
            lname_err.show('slow');
        }else{
            lname_err.hide('slow');
        }
        if((user_name == '') || (user_name.length <= 0)){
            error_count += 1;
            user_err.text("This Field cannot be blank");
            user_err.show('slow');
        }else{
            user_err.hide('slow');
        }
        if((email_address == '') || (email_address.length <= 0)){
            error_count += 1;
            email_err.text("This Field cannot be blank");
            email_err.show('slow');
        }else{
            email_err.hide('slow');
        }
        let status = validateEmail(email_address);
        if(!status){
            error_count += 1;
            email_err.html("Invalid email format<br>Email should be in the format mail@example.com");
            email_err.show('slow');
        }else{
            email_err.hide('slow');
        }
        if((password1 == '') || (password1.length <= 0)){
            error_count += 1;
            pass_err.text("This Field cannot be blank");
            pass_err.show('slow');
        }else{
            pass_err.hide('slow');
        }
        if(password1.length <= 7){
            error_count += 1;
            pass_err.text("Password should have a minimum length of 8 characters");
            pass_err.show('slow');
        }else{
            pass_err.hide('slow');
        }
        if((password2 == '') || (password2 !== password1)){
            error_count += 1;
            repass_err.text("Passwords do not match");
            repass_err.show('slow');
        }else{
            repass_err.hide('slow');
        }
        if(error_count === 0){
            $('#arena-signup').trigger('submit');
        }
    });

});