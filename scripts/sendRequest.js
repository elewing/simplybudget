$(document).ready(function(){
  $("#form_submit").click(send_ajax_request);
});

function sendBudget(e) {
  console.log(e.id);
  console.log(e.value);
  $.ajax({
    type: "POST",
    method: "POST",
    url: "/save-userinfo",
    data: {
      "category_name": e.id,
      "limit_amount": parseInt(e.value)
    }
  }).done(function() {
    console.log("Complete!");
  })
}

function send_ajax_request(e) {
  var form = $(e.currentTarget.parentElement);
  var statementElement = form.find(".c-select option:selected");
  var statementName = statementElement.data("file");
  var statementJSON = $.getJSON("/data/" + statementName + ".json", function(data){
    $.each(data, function(key, val){
      //do an ajax
      console.log(val);
      $.ajax({
        type: "GET",
        url: "/mc-handler",
        dataType: "xml",
        data: {
            url: "http://dmartin.org:8205",
            date: val[0],
            merchantid: val[1],
            price: val[2],
            statement_name: statementName
        }
      });
    });
  });
}
// $.ajax({
//   type: "GET",
//   url: "http://dmartin.org:8205",
//   dataType: "xml",
//   data: {
//     MerchantId: val[1]
//   }

//     }).done(function(xml){
//       console.log("GOT THE MC!");
//       var category = xmlParser(xml);
//       console.log(val[0]);
//       $.ajax({
//         type: "POST",
//         method: "POST",
//         url: "/save-post",
//         data: {
//           "statement_name": statementName,
//           "date": val[0],
//           "merchant_id": val[1],
//           "price_amount": parseFloat(val[2]),
//           "category": category
//         }
//       }).done(function(e){
//         console.log("Done!");
//       });
//     });
//   });
// }).fail(function(d, textStatus, error){
//   console.log("getJSON failed, status: " + textStatus + ", error: " + error);
// }).always(function(){
//   console.log("OH GOD");
// });
