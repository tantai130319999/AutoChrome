var debug = false;
var log = console.log;
var error = console.error;
if (!debug) { log = () => {}; error = () => {}; }

log("bg");

const DEFAULT_QUALITY_ICON = 8; // auto

browser.storage.sync.get().then(data => {
    let itemNum = data.qualityItemNum || null;

    if (!itemNum) {
        itemNum = DEFAULT_QUALITY_ICON;
        let qualityItemNum = 8;
        let quality = "tiny";
        browser.storage.sync.set({ qualityItemNum, quality });
    }

    new BrowserAction(itemNum);
});


browser.tabs.onUpdated.addListener((tabId, changeInfo, tabInfo) => {
	try {
		let url = tabInfo.url;
		let tabId = tabInfo.id;

		let anchor = document.createElement("a");
		anchor.href = url;

		if (anchor.host.includes("youtube.com")) {
			log("is youtube");

	        browser.tabs.sendMessage(tabId, {
	            message: "youtube-tab-updated",
	            url
	        });
		}
	} catch(ex) { 
		error(ex);
	}
});