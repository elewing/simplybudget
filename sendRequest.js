$(document).ready(function(){
  $("#form_submit").click(send_ajax_request);
});

function send_ajax_request(e) {
  var form = (e.currentTarget.parentElement);
  var statementId = form.find("#statementId")
  var statement = request_statement(statementId);
  for (var purchase in statement) {
    var queryUrl = "http://dmartin.org:8205" + purchase[1];
    $.ajax({
      url: "http://dmartin.org:8205" + purchase[1],
      dataType: "xml"
    }).done (function (xml) {
      xmlParser(xml);
    })
  }
}
