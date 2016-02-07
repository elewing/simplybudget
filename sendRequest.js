$(document).ready(function(){
  $("#form_submit").click(send_ajax_request);
});

function send_ajax_request(e) {
  var form = (e.currentTarget.parentElement);
  var statementId = form.find("#statementId")
  var statement = request_statement(statementId);
  for (var purchase in statement) {
    $.ajax({
      url: "http://dmartin.org:8205",
      type: "GET",
      dataType: "xml",
      data: {MerchantId:purchase[1]}
    }).done (function (xml) {
      var category = xmlParser(xml);
      $.ajax({
        type: "POST",
        method: "POST",
        url: "/save-statement",
        data: {
          "statement_name": statementId,
          "date": purchase[0],
          "merchant_id": purchase[1],
          "price": purchase[2],
          "category": category
        }
      })
    })
  }
}
