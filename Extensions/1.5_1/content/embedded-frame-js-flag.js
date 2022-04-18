class EmbeddedFrameJSFlag {
	constructor() {
		if (this.isHostYouTube() && 
			this.isEmbeddedFrame() && 
			!this.hasEmbeddedJSAPIFlag()) {
			this.addJSAPIFlag();
		}
	}

	isHostYouTube() {
		return window.location.host.includes("youtube.com");
	}

	isEmbeddedFrame() {
		return /^\/embed\//.test(window.location.pathname);
	}

	hasEmbeddedJSAPIFlag() {
		try {
			if (this.isSearchEmpty()) { return false; }

			let search = window.location.search.split("?")[1];
			search = search.split("&");

			return search.indexOf("enablejsapi=1") !== -1;
		} catch(ex) {
			error(ex);

			return false;
		}
	}

	isSearchEmpty() {
		return window.location.search === "";
	}

	addJSAPIFlag() {
		let flag = "";

		if (!this.isSearchEmpty()) { flag += "&"; }
		flag += "enablejsapi=1";

		window.location.search += flag;
	}
}

new EmbeddedFrameJSFlag();