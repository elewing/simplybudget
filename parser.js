
dictionary = ["SPORTING", "ElECTRONIC", "WEAR", "INNS", "FOOD",
              "RESTAURANTS", "EATING", "RENTAL", "STATIONS", "CREDIT",
            "COMPUTER", "ELECTRICAL", "RECORD"]

function xmlParser(xml) {
  var category = xml.getElementsbyTagName("MerchantCategory");
  var string = category[0].toString;
  var list = string.split(" ");
  var merchant;
  var group;
  for (i = 2; i < list.length; i++) {
    merchant.push(list[i].toString);
  }
  var string = "";
  for (i = 0; i < merchant.length; i++) {
    if (dictionary.contains(merchant[i])) {
      group = dictionary[i];
  }
}
  checkGroup(group);
}

function checkGroup(group) {
  var answer;
  if (["SPORTING", "RECORD", "CREDIT"].contains(group)) {
    answer = "entertainment";
  }
  else if (["RESTAURANTS", "EATING"].contains(group)) {
    answer = "eating out";
  }
  else if (["ELECTRONIC", "COMPUTER"].contains(group)) {
    answer = "electronics";
  }
  else if (["RENTAL", "INNS", "STATIONS"].contains(group)) {
    answer = "travel";
  }
  else if ("FOOD" === group) {
    answer = "groceries";
  }
  else if ("WEAR" === group) {
    answer = "clothing";
  }
  return answer;
}

//txt += merchant[i] + " ";
//for (i = 0; i < dictionary.length; i++) {
//if (txt.search(dictionary[i])) {
//var group = dictionary[i];
//}
//}
