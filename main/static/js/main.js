$('#add-order-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    $('#addOrderModal').modal('toggle');
    var url = "add-order/";
    create_post(url);
});

$('#change-order-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    var order_id = $('#order_change').data("id"),
    url = "/change-order/";
    console.log(order_id);
    create_post(url, order_id);
});

function create_post(url, order_id=null) {
    console.log("create post is working!");
    console.log($('#post-quickly').val())// sanity check
    $.ajax({
        url : url, // the endpoint
        type : "POST", // http method
        data : {
                    orderpk:order_id,
                    client_name:$('#post-client_name').val(),
                    phone:$('#post-phone').val(),
                    quickly:$('#post-quickly').val(),
                    device_type:$('#post-device_type').val(),
                    serial_number:$('#post-serial_number').val(),
                    brand:$('#post-brand').val(),
                    model:$('#post-model').val(),
                    equipment:$('#post-equipment').val(),
                    appearance:$('#post-appearance').val(),
                    password:$('#post-password').val(),
                    malfunction:$('#post-malfunction').val(),
                    receiver_notes:$('#post-receiver_notes').val(),
                    indicative_price:$('#post-indicative_price').val(),
                    executor:$('#post-executor').val(),
                    prepayment:$('#post-prepayment').val(),

                    availability_date:$('#post-availability_date').val(),
                    executor_note:$('#post-executor_note').val(),
                    verdict:$('#post-verdict').val(),
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
               }, // data sent with the post request

        // handle a successful response
        success : function(json) {

        if (json.flag == 1){
        console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            nowuiDashboard.showNotification('top','center');
        }
        else {
        location.reload();
            $('#post-client_name').val('');
            $('#post-phone').val('');
            $('#post-quickly').val('');
            $('#post-device_type').val('');
            $('#post-serial_number').val('');
            $('#post-brand').val('');
            $('#post-model').val('');
            $('#post-equipment').val('');
            $('#post-appearance').val('');
            $('#post-password').val('');
            $('#post-malfunction').val('');
            $('#post-receiver_notes').val('');
            $('#post-indicative_price').val('');
            $('#post-executor').val('');
            $('#post-prepayment').val('');
            $('#post-availability_date').val('');
            // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
            }
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};

$('#add-note-form').on('submit', function(event){
    event.preventDefault();
    console.log("вторая функция");
    var note_data = $('#postText').val(),
    id = $('#add_comment').data("id"),
    type = $('#add_comment').data("type");
    console.log(note_data);
    
    console.log(id);
    console.log(type);
    create_note(id, type);
});

function create_note (post_id, post_type){
    console.log("первая функция");
    console.log(post_id);
    console.log(post_type);
    var post_note = $('#postText').val();
    console.log(post_note);
    $.ajax({
        url:"/add-note/",
        type:"POST",
        data:{
            orderpk: post_id,
            note_data: post_note,
            type: post_type,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){
            $('#postText').val('');
            $('.notes').prepend(
                '<div class="card">' + '<div class="card-body">' + '<i class="now-ui-icons location_bookmark">' + '</i>' + '<p class="mb-auto">' + json.note_text +'</p>' +
                '</div>' + '</div>'
            )
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },
        error : function(xhr,errmsg,err) {
            console.log("error");
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
};

function showNotification(from, align){
    color = 'success';

    $.notify({
        icon: "now-ui-icons ui-1_bell-53",
        message: "Информация успешно обновлена."

      },{
          type: color,
          timer: 8000,
          placement: {
              from: from,
              align: align
          }
      });
}

$('#add-work-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    $('#addWorkModal').modal('toggle');
    var work_id = $('#add_work').data("id");
    console.log(work_id);
    create_work(work_id);
});

function create_work (work_id){
    var id = work_id;
    $.ajax({
        url:"/add-work/",
        type:"POST",
        data:{
            order_pk: work_id,
            work:$('#post-work').val(),
            amount: $('#post-amount').val(),
            price: $('#post-price').val(),
            warranty:$('#post-warranty').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){

            location.reload();
            $('#post-work').val('');
            $('#post-amount').val('');
            $('#post-price').val('');
            $('#post-warranty').val('');// remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },
        error : function(xhr,errmsg,err) {
            console.log("error");
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
};

$('#add-income-payment-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    $('#addIncomePaymentModal').modal('toggle');
    var type = "i", id = $('#add_income_payment').data("id"),
    description = $('#post-income-description').val(),
    total = $('#post-income-total').val();
    create_payment(type, id, description, total);
});

$('#add-consumption-payment-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    $('#addConsumptionPaymentModal').modal('toggle');
    var type = "c",
    id = $('#add_consumption_payment').data("id"),
    description = $('#post-consumption-description').val(),
    total = $('#post-consumption-total').val();
    create_payment(type, id, description, total);
});

function create_payment (payment_type, payment_id, payment_description, payment_total){
    $.ajax({
        url:"/add-payment/",
        type:"POST",
        data:{
            order_pk: payment_id,
            description: payment_description,
            total: payment_total,
            type: payment_type,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){

            location.reload();
            $('#post-description').val('');
            $('#post-total').val('');
            // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },
        error : function(xhr,errmsg,err) {
            console.log("error");
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
    });
};