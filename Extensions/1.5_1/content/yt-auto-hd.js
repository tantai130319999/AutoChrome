class YTAutoHD {
	constructor(quality = null) {
		this.quality = quality;
		this.player = null;
		this.currentUrl = null;

		this.updateCurrentURL();
	}

	async init() {
		try {
			ythdlog("init!!");
			this.player = await this.findPlayer();
			this.updatePlayerQuality();
			this.setMutationObserver();
		} catch(ex) {
			ythderror(ex);
		}
	}

	get Player() {
		return this.player;
	}

	setQuality(quality) {
		this.quality = quality;
	}

	updateCurrentURL() {
		this.currentUrl = window.location.href;
	}

	getPlayerElement() {
		return document.getElementById('movie_player') ||
			document.querySelector('.html5-video-player');
	}

	getAlternativeQuality() {
		let availableQualities = this.Player.getAvailableQualityLevels();

		if (availableQualities.length > 0) {
			return availableQualities[0];
		}

		return null;
	}

	isHostYouTube() {
		return window.location.host.includes("youtube.com");
	}	

	updatePlayerQuality() {
		try {
			// ythdlog("updatePlayerQuality");
			// ythdlog(this.quality);
			// ythdlog(this.Player.getAvailableQualityLevels());
			let isQualityAvaliable = this.player.getAvailableQualityLevels().includes(this.quality);
			let chosenQuality = isQualityAvaliable ? this.quality : this.getAlternativeQuality();
			
			if (chosenQuality === null) {
				throw new Error("YTAutoHD.updatePlayerQuality: 'chosenQuality' is null");
			}
			// ythdlog(isQualityAvaliable);
			// ythdlog(chosenQuality);
			this.player.setPlaybackQuality(chosenQuality);
			if (this.player.setPlaybackQualityRange) {
				this.player.setPlaybackQualityRange(chosenQuality);
			}
		} catch(ex) {
			ythderror(ex);
		}
	}

	findPlayer() {
		return new Promise((resolve, reject) => {
			if (!this.isHostYouTube()) { reject(); }
			let interval = setInterval(() => {
				ythdlog("trying to find player2");
				if (this.isPlayerExists()) {
					ythdlog("found it!!!");
					clearInterval(interval);
					resolve(this.getPlayerElement());
				}
			}, 500);
		});
	}

	isPlayerExists() {
		let player = document.getElementById('movie_player') 
			|| document.querySelector('.html5-video-player');
		ythdlog(player);

		return player && player.getAvailableQualityLevels().length !== 0;
	}

	setMutationObserver() {
		let target = this.player.querySelector(".video-stream") 
			|| this.player.querySelector(".html5-main-video");

		if (!target) { return; }

		let observerOptions = { attributes: true };
		let observer = new MutationObserver((mutationList, observer) => {
			mutationList.forEach((mutation) => {
			    switch(mutation.type) {
					case "attributes":
					if (mutation.attributeName === "src") {
						if (this.currentUrl !== window.location.href) {
							this.updateCurrentURL();
							this.updatePlayerQuality();
							// ythdlog("player changed");
						}
					}
					break;
			    }
			});
		});

		observer.observe(target, observerOptions);
	}

	static setDebug(debug) {
		if (debug) {
			Utils.appendScriptToDOM([ 
				"var ythdlog = console.log;",
				"var ythderror = console.error;"
			]);
		} else {
			Utils.appendScriptToDOM([
				"var ythdlog = () => {};",
				"var ythderror = () => {};"
			]);
		}
	}
}

YTAutoHD.DEFAULT_QUALITY = "hd720";