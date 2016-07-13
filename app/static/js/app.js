/**
 * Created by player3e on 2016. 7. 7..
 */

var AppEngine = {


    reqLogin : function() {
        var me = this;
        var data = {};
        data.memberId = $("#inputId").val();
        data.password = $("#inputPassword").val();

        $.ajax({
			url : '/auth/member/login.json',
			type : 'POST',
            data : JSON.stringify(data),
			async : false,
            contentType : 'application/json',
			dataType : 'json',
			success : function(data) {
				console.log(data)
                var resp = data
                if (resp['result'] == true) {
                    console.log('ok');
                    window.location.href = '/';
                }
                else {
                    alert(resp['message']);
                }
			},
			error : function(e) {
				console.log(e);
			}
		});
    },

    reqLogout : function() {
        var me = this;

        $.ajax({
			url : '/auth/member/logout.json',
			type : 'POST',
            data : '',
			async : false,
            contentType : 'application/json',
			dataType : 'json',
			success : function(data) {
				console.log(data)
                var resp = data
                if (resp['result'] == true) {
                    console.log('ok');
                    window.location.reload();
                }
                else {
                    alert(resp['message']);
                }
			},
			error : function(e) {
				console.log(e);
			}
		});
    }
}

$("#buttonLogin").on('click', function(e) {
        AppEngine.reqLogin();
});

$("#buttonLogout").on('click', function(e) {
        AppEngine.reqLogout();
});