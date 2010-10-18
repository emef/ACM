var merchant_id = "450045598351624",
	merchant_key = "SRPfHFxxbJBtDGg2jf0lEQ",
	url = "https://sandbox.google.com/checkout/api/checkout/v2/checkoutForm/Merchant/" + merchant_id;
function checkout(credit) {
	var f = document.createElement("form");
	function add_keyval(key,val) {
		var elem = document.createElement("input");
		elem.setAttribute("type", "hidden");
		elem.setAttribute("name", key);
		elem.setAttribute("value", val);
		f.appendChild(elem);
	}
	f.setAttribute("method", "POST");
	f.setAttribute("action", url);
	add_keyval("item_name_1", "ACM Cabinet Credit");
	add_keyval("item_description_1", "Credit to use for buying stuff from the ACM cabinet in CF405.");
	add_keyval("item_price_1", credit);
	add_keyval("item_currency_1", "USD");
	add_keyval("item_quantity_1", "1");
	add_keyval("item_merchant_id_1", merchant_id);
	f.submit();
}
