window.onload = function() {
	var cart = { total:0.0 },
		items = document.getElementById("items").children,
		p = /(.+) \(\$([\d.]+)\) ID#(\d+)/,
		item,m;
	for(var i=0, j=items.length; i < j; i++) {
		item = items[i];
		m = item.children[0].innerText.match(p);
		item.onclick=(function(name, price, id) {
			return function() {
				cart[id] ? cart[id] = [name, cart[id][1]+1]
						 : cart[id] = [name, 1];
				cart.total += parseFloat(price);
				updateCartDiv(cart);
			}
		})(m[1], m[2], m[3]);
	}
	document.getElementById("purchase").onclick = function() {
		var form = document.getElementById("purchase_form"),
			data = document.createElement("input");
		form.setAttribute("action", "checkout");
		form.setAttribute("method", "POST");
		data.setAttribute("type", "hidden");
		data.setAttribute("name", "data");
		data.setAttribute("value", JSON.stringify(cart));
		//form.appendChild(data);
		console.log(JSON.stringify(cart));
		form.submit();
	}
}

function updateCartDiv(cart) {
	var d = document.createElement("div"),
		cartDiv = document.getElementById("cart"),
		elem, total=0;
	for(i in cart) {
		if (i != "total") {
			elem = document.createElement("div");
			elem.innerText = cart[i][1] + " x " + cart[i][0];
			d.appendChild(elem);
		}
	}
	d.setAttribute("class", "cart_items");
	cartDiv.replaceChild(d, cartDiv.children[1]);
	document.getElementById("cart_total").innerText = cart.total.toFixed(2);
}
