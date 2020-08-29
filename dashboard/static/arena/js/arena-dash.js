// Storing profile details globally
let profile_fname = ''; let profile_lname = ''; let profile_email = ''; let profile_username = '';
let profile_phone = ''; let profile_about = ''; let profile_pubId = '';
let app = new Vue({
    el:'#arena-dashboard',
    delimiters:['[[', ']]'],
    data:{
        toggle_name_edit:false, email_edit_toggle:false, toggle_username_edit: false, toggle_pass_edit: false,
        toggle_phone_edit: false, toggle_bio_edit: false, toggle_pubId_edit: false,
        first_name:'',last_name:'', username:'', email: '',
        passcode:'', repasscode: '', phone_number:'', about:'', pub_id: '', msg: '',
        err_block_class: ''
    },
    created:function(){
        // Prefetch user details when created
        this.get_user_details();
    },
    methods:{
        editFullName: function(event, val){
            event.preventDefault();
            if((this.first_name.length || this.last_name.length) > 0){
                this.update_details(val);
            }
            this.toggle_name_edit = !this.toggle_name_edit;
            window.setTimeout(function () {
                $('#fname').text(profile_fname + ' ' + profile_lname);
            }, 500);
        },
        toggle_full_name_edit:function(event){
            event.preventDefault();
            // Assign values so that it reflects in HTML DOM elements where v-model is applied
            this.first_name = profile_fname;
            this.last_name = profile_lname;
            this.toggle_name_edit = !this.toggle_name_edit;
            // Apply delay so that element displays before changing inner element text
            if(!this.toggle_name_edit){
                window.setTimeout(function () {
                    $('#fname').text(profile_fname + ' ' + profile_lname);
                    if((profile_fname == null && profile_lname == null) || (profile_fname == '' && profile_lname == '')){
                        $('#fname').text('No Name');
                    }else{
                        $('#fname').text(profile_fname + ' ' + profile_lname);
                    }
                }, 1);
            }
        },
        editUsername: function(event, val){
            event.preventDefault();
            if(this.username.length > 0){
                this.update_details(val);
            }
            this.toggle_username_edit = !this.toggle_username_edit;
            window.setTimeout(function () {
                $('.js-uname').text(profile_username);
            }, 500);
        },
        toggle_user_name_edit:function(event){
            event.preventDefault();
            // Assign value so that it reflects in HTML DOM elements where v-model is applied
            this.username = profile_username;
            this.toggle_username_edit = !this.toggle_username_edit;
            if(!this.toggle_username_edit){
                window.setTimeout(function () {
                    $('.js-uname').text(profile_username);
                }, 1);
            }
        },
        editEmail: function(event, val){
            event.preventDefault();
            if(this.email.length > 0){
                this.update_details(val);
            }
            this.email_edit_toggle = !this.email_edit_toggle;
            window.setTimeout(function () {
                $('.js-email').text(profile_email)
            }, 500);
        },
        toggle_Email_edit:function(event){
            event.preventDefault();
            // Assign value so that it reflects in HTML DOM elements where v-model is applied
            this.email = profile_email;
            this.email_edit_toggle = !this.email_edit_toggle;
            if(!this.email_edit_toggle){
                window.setTimeout(function () {
                    if(profile_email == null || profile_email == ''){
                        $('.js-email').text('No Email Address');
                    }else{
                        $('.js-email').text(profile_email)
                    }
                }, 1);
            }
        },
        editPassword: function(event, val){
            event.preventDefault();
            if(this.passcode.length > 0){
                this.update_details(val);
            }
            this.toggle_pass_edit = !this.toggle_pass_edit;
            this.passcode = '';
        },
        toggle_password_edit:function(event){
            event.preventDefault();
            this.toggle_pass_edit = !this.toggle_pass_edit;
            // Assign value so that it reflects in HTML DOM elements where v-model is applied
            this.passcode = '';
        },
        editPhone: function(event, val){
            event.preventDefault();
            if(this.phone_number !== null){
                if(this.phone_number.length > 0){
                    this.update_details(val);
                }
            }
            this.toggle_phone_edit = !this.toggle_phone_edit;
            window.setTimeout(function () {
                if(profile_phone !== null){
                    $('#d-phone').text(profile_phone)
                }else{
                    $('#d-phone').text('No Phone Number');
                }
            }, 500);
        },
        toggle_phonenumber_edit:function(event){
            event.preventDefault();
            // Assign value so that it reflects in HTML DOM elements where v-model is applied
            this.phone_number = profile_phone;
            this.toggle_phone_edit = !this.toggle_phone_edit;
            if(!this.toggle_phone_edit){
                window.setTimeout(function () {
                    if(profile_phone == null || profile_phone == ''){
                        $('#d-phone').text('No Phone Number');
                    }else{
                        $('#d-phone').text(profile_phone);
                    }

                }, 1);
            }

        },
        editAbout: function(event, val){
            event.preventDefault();
            if(this.about !== null){
                if(this.about.length > 0){
                    this.update_details(val);
                }
            }
            this.toggle_bio_edit = !this.toggle_bio_edit;
            window.setTimeout(function () {
                if(profile_about !== null){
                    $('#d-about').text(profile_about);
                }else{
                    $('#d-about').text('No bio');
                }
            }, 500);
        },
        toggle_about_edit:function(event){
            event.preventDefault();
            // Assign value so that it reflects in HTML DOM elements where v-model is applied
            this.about = profile_about;
            this.toggle_bio_edit = !this.toggle_bio_edit;
            if(!this.toggle_bio_edit){
                window.setTimeout(function () {
                    if(profile_about == null || profile_about == ''){
                        $('#pubId').text('No Bio');
                    }else{
                        $('#d-about').text(profile_about);
                    }
                }, 1);
            }

        },
        editPubId: function(event, val){
            event.preventDefault();
            if(this.pub_id !== null){
                if(this.pub_id.length > 0){
                    this.update_details(val);
                }
            }
            this.toggle_pubId_edit = !this.toggle_pubId_edit;
            window.setTimeout(function () {
                if(profile_pubId !== null){
                    $('#pubId').text(profile_pubId);
                }else{
                    $('#pubId').text('No Public id (username will be used)');
                }
            }, 500);
        },
        toggle_pub_id_edit:function(event){
            event.preventDefault();
            // Assign value so that it reflects in HTML DOM elements where v-model is applied
            this.pub_id = profile_pubId;
            this.toggle_pubId_edit = !this.toggle_pubId_edit;
            if(!this.toggle_pubId_edit){
                window.setTimeout(function () {
                    if(profile_pubId == null || profile_pubId == ''){
                        $('#pubId').text('No Public id (username will be used)');
                    }else{
                        $('#pubId').text(profile_pubId);
                    }
                }, 1);
            }
        },
        update_details: function(val){
            switch(val) {
                case 1: // to update first name and last name
                    let fname = this.first_name;
                    let lname = this.last_name;
                    this.ajax_profile_request(fname, lname);
                    break;
                case 2: // Update Username
                    let uname = this.username;
                    this.ajax_profile_request('','',uname);
                    break;
                case 3: // Update email
                    let email = this.email;
                    this.ajax_profile_request('', '', '', email);
                    break;
                case 4: // Update Password
                    let passcode = this.passcode;
                    this.ajax_profile_request('', '', '', '', passcode);
                    break;
                case 5: // Update Phone
                    let phone = this.phone_number;
                    this.ajax_profile_request('', '', '', '', '', phone);
                    break;
                case 6: // Update Bio
                    let bio = this.about;
                    this.ajax_profile_request('', '', '', '', '', '', bio);
                    break;
                case 7: // Update public name
                    let pub_id = this.pub_id;
                    this.ajax_profile_request('', '', '', '', '', '', '', pub_id);
                    break;
                default:
                    break;
            }

        },
        ajax_profile_request: function(fname, lname, user_name, email, passcode, pnumber, about, pubId){
            if(fname !== '' || lname !== '' || user_name !== '' || email !== '' || passcode !== '' || pnumber !== ''
                || about !== '' || pubId !== ''){
                let status = false;
                $.ajax({
                    url: 'ajax/update_profile/',
                    type: 'POST',
                    data:{
                        first_name: fname,
                        last_name: lname,
                        username:user_name,
                        email: email,
                        passcode: passcode,
                        pnumber: pnumber,
                        about: about,
                        pub_id: pubId
                    },
                    dataType: 'json',
                    success: function(data){
                        // When update request is confirmed update global registered profile values
                        // alert('profile updated successfully');
                        profile_fname = data['fname'];
                        profile_lname = data['lname'];
                        profile_email = data['email'];
                        profile_username = data['username'];
                        profile_phone = data['phone'];
                        profile_about = data['about'];
                        profile_pubId = data['pubId'];
                        setTimeout(function(){
                            this.display_success_msg('Success', 'Profile Successfully Updated !');
                        });
                    },
                    error:function(){
                       setTimeout(function(){
                            this.display_error_msg('Error', 'Profile Update Error please check internet connection');
                        });
                    }
                });
            }
        },
        get_user_details: function(){
            /***
             * Function to pre-fetch user details and store to globally registered variables
             */
            $.ajax({
                url: 'ajax/get_profile/',
                dataType: 'json',
                success: function (data) {
                    // Assign fetched values to global variables
                    // $('#dash_fname').val(data.first_name);
                    // $('#dash_lname').val(data.last_name);
                    profile_fname = data['first_name'];
                    profile_lname = data['last_name'];
                    profile_email = data['email'];
                    profile_username = data['username'];
                    profile_phone = data['phone_number'];
                    profile_about = data['about'];
                    profile_pubId = data['pub_id'];
                }
            });
        },
    }
});
function display_success_msg(head, message){
    let err_block =  $('.dash-err-block');
    let err_block_heading = $('.dash-err-block .alert-heading');
    let err_block_content = $('.dash-err-block .alert-content');
    err_block_heading.text(head.toString());
    err_block_content.text(message.toString());
    err_block.fadeIn(1000).delay(2000).fadeOut(1000);
}
function display_error_msg(head, message){
    let err_block =  $('.dash-err-block');
    let err_block_heading = $('.dash-err-block .alert-heading');
    let err_block_content = $('.dash-err-block .alert-content');
    err_block_heading.text(head.toString());
    err_block_content.text(message.toString());
    err_block.addClass('alert-danger');
    err_block.fadeIn(1000).delay(2000).fadeOut(1000);
    setTimeout(function(){
        err_block.removeClass('alert-danger');
    },4000)
}