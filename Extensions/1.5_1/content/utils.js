class Utils {
	static appendScriptToDOM(scriptLinesArray) {
		const ELEMENT_ID = `youtube-hd-${browser.runtime.id}`;

		if (document.getElementById(ELEMENT_ID)) {
			document.getElementById(ELEMENT_ID).remove();
		}

		let script = document.createElement("script");
		script.textContent = scriptLinesArray.join(';');
		script.id = ELEMENT_ID;

		document.documentElement.appendChild(script);
	}

	static isHostYouTube() {
		return window.location.host.includes("youtube.com");	
	}
}