function updateemail() {
    $.post('http://muki.webfactional.com/api/ciljesled/updateemail/', {
        fbid: fbid,
        email: $('#email').val()
    }, function (r) {
        if (r == 1) {
            sweetAlert('Email naslov uspešno posodobljen.', '', 'success');
        } else {
            sweetAlert('Ups, nekaj je šlo narobe.', '', 'error');
        }
    })
}

function updatename() {
    $.post('http://muki.webfactional.com/api/ciljesled/updatename/', {
        fbid: fbid,
        name: $('#name').val()
    }, function (r) {
        if (r == 1) {
            sweetAlert('Ime uspešno posodobljeno.', '', 'success');
        } else {
            sweetAlert('Ups, nekaj je šlo narobe.', '', 'error');
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