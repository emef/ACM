window.onload = function() {
	var cart = {},
		items = document.getElementById("items").children,
		p = /(.+) \(\$([\d.]+)\) ID#(\d+)/,
		item,m,total=0.0;
	for(var i=0, j=items.length; i < j; i++) {
		item = items[i];
		m = item.children[0].innerText.match(p);
		item.onclick=(function(name, price, id) {
			return function() {
				cart[id] ? cart[id] = { name: name, quantity: cart[id].quantity+1 }
						 : cart[id] = { name: name, quantity: 1 };
				total += parseFloat(price);
				updateCartDiv(cart, total);
			}
		})(m[1], m[2], m[3]);
	}
	document.getElementById("purchase").onclick = function() {
		var form = document.getElementById("purchase_form"),
			data = document.createElement("input"),
			wnumber = document.getElementById("wnumber").value,
			error = document.getElementById("wnumber_error"),
			p = /\d{8}/;

		// little validation
		if(!p.test(wnumber)) {
			error.innerText = "WNumber required";
			return;
		} else if (empty(cart)) {
			error.innerText = "Empty cart";
			return;
		}

		// add items and go
		addKeyVal(form, "data", JSON.stringify(cart));
		addKeyVal(form, "wnumber", wnumber); 
		form.submit();
	}
}

function updateCartDiv(cart, total) {
	var d = document.createElement("div"),
		cartDiv = document.getElementById("cart"),
		elem, total=0;
	for(i in cart) {
		if (i != "total") {
			elem = document.createElement("div");
			elem.innerText = cart[i].quantity + " x " + cart[i].name;
			d.appendChild(elem);
		}
	}
	d.setAttribute("class", "cart_items");
	cartDiv.replaceChild(d, cartDiv.children[1]);
	document.getElementById("cart_total").innerText = total.toFixed(2);
}

function addKeyVal(form, key, val) {
	var data = document.createElement("input");
	data.setAttribute("type", "hidden");
	data.setAttribute("name", key);
	data.setAttribute("value", val);
	form.appendChild(data);
}

function empty(obj) {
	for(i in obj) {
		return false;
	}
	return true;
}
