$(function(){

    $('#arena-acc').click(preventLinkClick);
    $('#arena-acc-m').click(preventLinkClick);

    // insert new element to display username validation message
    $('#user').before("<span id='user-msg'></span>");

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
                    userblock.html("<p style='color:red'>" + data['error_message'] + "</p>");
                }else{
                    userblock.html("");
                }
            }
        });
    });

    function preventLinkClick(event){
        event.preventDefault();
        $("#arena-account").modal();
    }
});