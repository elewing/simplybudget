$(document).ready(function(){
  $("#form_submit").click(send_ajax_request);
});

function sendBudget(e) { 
  $.ajax({
    type: "POST",
    method: "POST",
    url: "/save-userinfo",
    data: {
      "category_name": e.id,
      "limit_amount": e.value
    }
  }).done(function() {
    console.log("Complete!");
  })
}

function send_ajax_request(e) {
  _this = this;
  var form = (e.currentTarget.parentElement);
  var statementName = form.find(".dropdown-menu option:selected").val();

  var statementJSON = $.getJSON("/data/" + statementName, function(data){
    $.each(data, function(key, val){
      __this = this;
      //do an ajax
      $.ajax({
        type: "GET",
        url: "http://dmartin.org:8205",
        dataType: "xml",
        data: {
          "MerchantId": val[1]
        }
      }).done(function(xml){
        var category = xmlParser(xml);
        console.log(val[0]);
        $.ajax({
          type: "POST",
          method: "POST",
          url: "/save-post",
          data: {
            "statement_name": statementName,
            "date": val[0],
            "merchant_id": val[1],
            "price_amount": val[2],
            "category": category
          }
        }).done(function(e){
          console.log("Done!");
        });
      });
    });
  });
}
