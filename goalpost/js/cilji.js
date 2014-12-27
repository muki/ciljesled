var goalHTML = ['<div class="row">',
                '<div class="col-md-6 goaltitle">',
                '<h3><span class="goaltitlespan">{{ goal }}</span> <span class="deleteme glyphicon glyphicon-trash"></span></h3>',
                '</div>',
                '<div class="col-md-6">',
                '<h3 class="pull-right">{{ deadline }}</h3>',
                '</div>',
                '</div>',
                '<div class="row">',
                '<div class="col-md-12">',
                '<div class="cilj">',
                '<div class="progress">',
                '<div class="ciljprogress progress-bar progress-bar-warning progress-bar-striped" role="progressbar" aria-valuenow="{{ nowdiffdays }}" aria-valuemin="0" aria-valuemax="{{ totaldiffdays }}" style="width: {{ percentage }}%">',
                '{{ nowdiff }} left.',
                '</div>',
                '</div>',
                '</div>',
                '</div>',
                '</div>'].join('');

var goalsdownloaded = false;

function dostuff() {

    if (!goalsdownloaded) {

        $.get('http://muki.webfactional.com/api/ciljesled/getgoals/?fbid=' + fbid, function (response) {
            for (goalindex in response) {

                var deadline = moment(response[goalindex]['deadline'], 'DD. MM. YYYY');
                var start = moment(response[goalindex]['start'], 'DD. MM. YYYY');

                var totaldiff = moment.duration(deadline.diff(start));
                var nowdiff = moment.duration(deadline.diff(moment()));

                var totaldiffdays = moment.duration(deadline.diff(start)).asDays();
                var nowdiffdays = moment.duration(deadline.diff(moment())).asDays();

                var percentage = nowdiffdays / totaldiffdays * 100;

                console.log(totaldiff.humanize(), nowdiff.humanize());

                // manipulate HTML

                var newHTML = goalHTML
                    .replace(/{{ goal }}/g, response[goalindex]['goal'])
                    .replace(/{{ deadline }}/g, response[goalindex]['deadline'])
                    .replace(/{{ nowdiff }}/g, nowdiff.humanize())
                    .replace(/{{ totaldiff }}/g, totaldiff.humanize())
                    .replace(/{{ nowdiffdays }}/g, nowdiffdays)
                    .replace(/{{ totaldiffdays }}/g, totaldiffdays)
                    .replace(/{{ percentage }}/g, percentage);

                $('.controls')
                    .before(newHTML);

                goalsdownloaded = true;

            }
        });
    }

}

function postnewgoal() {

    if ($('#goaltitle').val() == '' || $('#goaldeadline').val() == '') {
        sweetAlert('Please fill in all fields marked with an asterisk.', '', 'warning');
    } else {

        $.post('http://muki.webfactional.com/api/ciljesled/addgoal/', {
            fbid: fbid,
            deadline: $('#goaldeadline').val(),
            goal: $('#goaltitle').val(),
            description: $('#goaldescription').val()
        }, function (r) {
//            console.log(r);
            document.location.reload();
        });
    }
}

function deletegoal(goaltitle) {
    $.post('http://muki.webfactional.com/api/ciljesled/deletegoal/', {
        fbid: fbid,
        goal: goaltitle
    }, function(r) {
        console.log(r);
        sweetAlert('Goal successfully deleted!', '', 'success');
        document.location.reload();
    });
}

$(document).ready(function () {
    $('#goaldeadline').datepicker();
    
    $('#savegoal').on('click', function() {
        postnewgoal();
    });
    
    $('.cilji').on('mouseenter', '.goaltitle', function() {
        console.log(this);
        $(this)
            .children('h3')
                .children('.deleteme')
                    .css('color', '#000000');
    });
    $('.cilji').on('mouseleave', '.goaltitle', function() {
        $(this)
            .children('h3')
                .children('.deleteme')
                    .css('color', '#ffffff');
    });
    
    $('.cilji').on('click', '.deleteme', function() {
        
        deletegoal($(this).prev().text());
        
    });
});