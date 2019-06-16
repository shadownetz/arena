let app = new Vue({
    el:'#arena-dashboard',
    delimiters:['[[', ']]'],
    data:{
        toggle_name_edit:false,first_name:'',last_name:'', username:'',
        passcode:'', phone_number:'', about:'', pub_id: '',
    },
    computed:{
        // get_profile_object:function(){
        //     $.ajax({
        //         url: 'ajax/get_profile/',
        //         dataType: 'json',
        //         success: function(data){
        //             this.first_name = data['first_name'];
        //             this.last_name = data['last_name'];
        //             this.username = data['username'];
        //             this.phone_number = data['phone_number'];
        //             this.about = data['about'];
        //             this.pub_id = data['pub_id'];
        //             alert(this.first_name);
        //         }
        //     });
        // },
    },
    methods:{
        editFullName: function(event, val){
            event.preventDefault();
            if((this.first_name.length || this.last_name.length) > 0){
                this.update_details(event, val);
            }
            this.toggle_name_edit = !this.toggle_name_edit;
            this.first_name = this.last_name = '';
        },
        toggle_full_name_edit:function(event){
            event.preventDefault();
            this.toggle_name_edit = !this.toggle_name_edit;
            this.first_name = this.last_name = '';
        },
        update_details: function(event, val){
            event.preventDefault();
            switch(val) {
                // to update first name and last name
                case 1:
                    let fname = this.first_name;
                    let lname = this.last_name;
                    this.ajax_profile_request({'first_name': fname, 'last_name': lname});
                    break;
            }

        },
        ajax_profile_request: function(data_object){
            if(data_object !== ''){
                $.ajax({
                    url: 'ajax/update_profile/',
                    type: 'POST',
                    data:{
                        'data_object': data_object
                    },
                    dataType: 'json',
                    success: function(data){
                        alert('profile updated successfully')
                    },
                    error:function(){
                        alert('An error occurred')
                    }
                });
            }
        }
    }
});