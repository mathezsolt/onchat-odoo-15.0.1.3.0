/** @odoo-module */
import { useService } from "@web/core/utils/hooks";
import { MainComponentsContainer } from "@web/core/main_components_container"
import { session } from "@web/session";
import { patch } from "@web/core/utils/patch";

const { onMounted } = owl.hooks;

patch(MainComponentsContainer.prototype, "onchat_bits.MainComponentsContainerPatch", {
    setup() {
        this._super(...arguments);
        this.httpService = useService("http");
        const body = document.getElementsByTagName('head')[0];
        this.rpc = useService("rpc");
        onMounted(async() => {
            const chatbot = await this.rpc("/get/chatbot");
            if(chatbot) {
                const script = document.createElement("script");
                script.type = "text/javascript";
				script.src = "https://onchat.ai/onchat.js?bot="+chatbot.id;
                script.async = true;
                const chatScript = document.getElementById(chatbot);
                if(chatScript && chatScript.length > 0) {
                    return;
                } else {
					if(session.is_frontend) {
						if(window.self !== window.top) {
							return;
						} else {
							body.appendChild(script);
						}
					} else {
						body.appendChild(script);
					}
                }
            }
        })
    },
})
