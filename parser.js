
function xmlParser(xml) {
  var category = xml.getElementsbyTagName("MerchantCategory");
  var string = category[0].toString;
  var list = string.split(" ");
  var merchant;
  for (i = 0; i < list.length; i++) {
    if (typeof list[0] !== Number) {
      merchant.push(list[0]);
    }
  }
  var string = "";
  for (i = 0; i < merchant.length; i++) {
    txt += merchant[i] + " ";
  }
}

dictionary = ["SPORTING", "ElECTRONIC", "WEAR", "INNS", "FOOD",
              "RESTAURANTS", "EATING", "RENTAL", "STATIONS", "CREDIT",
            "COMPUTER", "ELECTRICAL", "RECORD"]
