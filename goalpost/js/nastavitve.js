function updateemail() {
    $.post('http://muki.webfactional.com/api/ciljesled/updateemail/', {
        fbid: fbid,
        email: $('#email').val()
    }, function (r) {
        if (r == 1) {
            sweetAlert('Email address successfully updated.', '', 'success');
        } else {
            sweetAlert('Ooops, something went wrong.', '', 'error');
        }
    })
}

function updatename() {
    $.post('http://muki.webfactional.com/api/ciljesled/updatename/', {
        fbid: fbid,
        name: $('#name').val()
    }, function (r) {
        if (r == 1) {
            sweetAlert('Name and last name successfully updated.', '', 'success');
        } else {
            sweetAlert('Ooops, something went wrong.', '', 'error');
        }
    })
}

function dostuff() {
    $.get('http://muki.webfactional.com/api/ciljesled/getuserinfo/?fbid=' + fbid, function (r) {
        $('#name').val(r['name']);
        $('#email').val(r['email']);
    });
}

$(document).ready(function () {
    $('#updatename').on('click', function() {
        updatename();
    });
    $('#updateemail').on('click', function() {
        updateemail();
    });
});