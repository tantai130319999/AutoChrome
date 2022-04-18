var LocaleBinder = (function() {
	const DATA_ATTRIBUTE_LOCALE = "data-locale";
	const DATA_ATTRIBUTE_LOCALE_INNER_HTML = "data-locale-inner";

	class LocaleBinder {
		constructor() {
			this.bind();
		}

		getAllElementsWithDataAttribute() {
			return document.querySelectorAll("[" + DATA_ATTRIBUTE_LOCALE + "]");
		}

		bind() {
			try {
				let elements = this.getAllElementsWithDataAttribute();

				for (let i = 0; i < elements.length; i++) {
					let element = elements[i];

					if (this.hasLocaleForInnerHtml(element)) {
						this.setLocaleForInnerHtml(element);
					}

					this.setLocalesForAttributes(element);
				}
			} catch(ex) {
				error(ex);
			}
		}

		getLocaleValueForInnerHtml(element) {
			if (element.hasAttribute(DATA_ATTRIBUTE_LOCALE_INNER_HTML)) {
				let localeValue = element.getAttribute(DATA_ATTRIBUTE_LOCALE_INNER_HTML);
				localeValue = localeValue.trim();

				if (!localeValue) {
					return null;
				}

				return browser.i18n.getMessage(localeValue);
			}

			return null;
		}

		hasLocaleForInnerHtml(element) {
			return element.hasAttribute(DATA_ATTRIBUTE_LOCALE_INNER_HTML);
		}

		setLocaleForInnerHtml(element) {
			let innerHtmlLocaleValue = this.getLocaleValueForInnerHtml(element);
			if (innerHtmlLocaleValue) {
				this.setTextNode(element, innerHtmlLocaleValue);
			}
		}

		setTextNode(element, text) {
			for (let node of element.childNodes) {
				if (node.nodeType === 3) {
					node.nodeValue = text;

					return;
				}
			}
		}

		setLocalesForAttributes(element) {
			for (let localeKey in element.dataset) {
				let localeValue = element.dataset[localeKey];
				let targetAttributeName = this.extractTargetAttributeName(localeKey);
				if (targetAttributeName && element.hasAttribute(targetAttributeName)) {
					element.setAttribute(targetAttributeName, browser.i18n.getMessage(localeValue));
				}
			}
		}

		extractTargetAttributeName(localeKey) {
			return localeKey.split("locale")[1].toLowerCase();
		}
	}

	return LocaleBinder;
})();