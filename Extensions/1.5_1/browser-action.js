var BrowserAction = (function() {
    const ICON_QUALITY_PATH_MAP = {
        _0: "../images/qualities/4320.png",
        _1: "../images/qualities/2160.png",
        _2: "../images/qualities/1440.png",
        _3: "../images/qualities/1080.png",
        _4: "../images/qualities/720.png",
        _5: "../images/qualities/480.png",
        _6: "../images/qualities/360.png",
        _7: "../images/qualities/240.png",
        _8: "../images/qualities/144.png",
        _9: "../images/hd_128.png",
        DEFAULT: "../images/hd_128.png"
    };

    class BrowserAction {
        constructor(itemNum = null) {
            if (itemNum) {
                this.setIcon(itemNum);
            }
        }

        setIcon(itemNum) {
            let path = ICON_QUALITY_PATH_MAP[`_${itemNum}`] || ICON_QUALITY_PATH_MAP.DEFAULT;
            browser.browserAction.setIcon({ path });
        }
    }

    return BrowserAction;
})();