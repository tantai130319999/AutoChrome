var debug = false;
var log = console.log;
var error = console.error;
if (!debug) { log = () => {}; error = () => {}; }

class Main {
	constructor() {
		this.lastUrl = null;
		
		YTAutoHD.setDebug(debug);
		this.init();
	}

	async init() {
		if (!Utils.isHostYouTube()) { return; }

		let settings = await this.getSettings();
		let quality = this.getDefaultQuality(settings);

		Utils.appendScriptToDOM([
			YTAutoHD.toString(),
			`var ytAutoHD = new YTAutoHD('${quality}');`,
			`ytAutoHD.init();`
		]);

		this.setListeners();
	}

	getDefaultQuality(settings = {}) {
		return settings.quality ? settings.quality : ytAutoHD.DEFAULT_QUALITY;
	}

	setListeners() {
		browser.runtime.onMessage.addListener((request, sender, sendResponse) => {
			log(request.message);
			
			if (request.message === "quality-updated") {
				this.triggerSetQualityScript(request.quality);
				this.triggerUpdatePlayerQualityScript();
			}

			if (request.message === "youtube-tab-updated") {
				if (this.lastUrl !== request.url) {
					setTimeout(()=>{
						this.triggerUpdatePlayerQualityScript();
					}, 1000);

					this.lastUrl = request.url;
					log("url updated");
				}
			}
		});
	}

	triggerUpdatePlayerQualityScript() {
		Utils.appendScriptToDOM([
			`try { ytAutoHD.updatePlayerQuality(); } catch(ex) { ythderror(ex); }`
		]);
	}

	triggerSetQualityScript(quality) {
		Utils.appendScriptToDOM([
			`try { ytAutoHD.setQuality('${quality}'); } catch(ex) { ythderror(ex); }`
		]);
	}

	async getSettings() {
		return browser.storage.sync.get();
	}
}

var main = new Main();