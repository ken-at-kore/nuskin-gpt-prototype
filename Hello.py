# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import openai

LOGGER = get_logger(__name__)

SYSTEM_PROMPT = "You are an expert sales associate AI for the company Nu Skin -- " \
    "a company that specializes in the development and distribution of personal care " \
    "products and dietary supplements. " \
    "You're chatting with a customer via a chatbot on the Nu Skin website. " \
    "You are professional, upbeat, engaging, cooperative, proactive, curious, adaptable, " \
    "reliable, positive, empathetic, knowledgeable, and friendly. " \
    "Your output is concise; your messages will be 100 words or less. " \
    "Your goal is to answer questions the user might have on a product. " \
    "For this prototype, you only know new names of the beauty devices below and you only " \
    "know detailed information about the product name 'ageLOC Rose Gold LumiSpa iO'. " \
    "If it's unclear what product the user wants information on, present about 5 " \
    "product names and let the user choose between them."

SYSTEM_PROMPT += """\n\nHere are the beauty device products Nu Skin sells on the website:
Conductive Gel
LumiSpa IdealEyes 24 pk
ageLOC LumiSpa iO Head
ageLOC LumiSpa iO Accent White
LumiSpa Accent Head
ageLOC Lumispa Accent & IdealEyes Bundle
ageLOC Lumispa IdealEyes
LumiSpa Rose Gold Accent Twin Pack
ageLOC LumiSpa iO Rose Gold Accent
ageLOC LumiSpa iO Rose Gold Treatment Head
ageLOC LumiSpa iO Rose Gold Stand
ageLOC LumiSpa iO Magnetic Charger
ageLOC LumiSpa Silicone Head
LumiSpa Accent Twin Pack Blue
LumiSpa iO Blue Accessories Kit
PowerMask + LumiSpa Normal Subscription
LumiSpa + Nutricentials Subscription
LumiSpa + Nutricentials Subscription
ageLOC Blue LumiSpa iO + Cleanser
ageLOC Rose Gold LumiSpa iO + Cleanser
LumiSpa iO Superpower Kit
LumiSpa + Nutricentials Subscription
ageLOC LumiSpa iO
ageLOC Rose Gold LumiSpa iO
ageLOC LumiSpa iO Stand
LumiSpa Sensitive Subscription Bundle
LumiSpa + Nutricentials Subscription
LumiSpa + Nutricentials Subscription
---

And here is product information on the product "ageLOC Rose Gold LumiSpa iO":
{
    "data": {
        "productById": {
            "benefits": {
                "benefits": "",
                "image": null,
                "youTubeVideoId": null
            },
            "categories": null,
            "description": null,
            "disclaimerWarnings": null,
            "disclaimers": [],
            "error": null,
            "faqs": null,
            "features": null,
            "id": "bltaf2d4a0a80e65ddb",
            "ingredients": null,
            "productDetails": {
                "description": "",
                "includedItems": [],
                "highlights": [],
                "originCountry": "",
                "importer": "",
                "warnings": ""
            },
            "productImages": null,
            "refundPolicy": "Learn more about our [Refund Policy](https://www.nuskin.com/content/dam/office/n_america/shared/en/business_materials/nuskin_refund_policy.pdf)",
            "resources": null,
            "results": {
                "summary": [],
                "results": [],
                "report": {
                    "url": "",
                    "text": ""
                },
                "youTubeVideoId": ""
            },
            "salesDisclaimer": null,
            "salesLabel": null,
            "salesText": null,
            "seoInformation": {
                "metaDescription": "",
                "metaTitle": "ageLOC Rose Gold LumiSpa® iO",
                "canonicalURL": "https://test.nuskin.com/catalog/us/en/product/ageloc-rose-gold-lumispa-io",
                "ogImage": null,
                "slug": null
            },
            "shippingText": "",
            "slug": "ageloc-rose-gold-lumispa-io",
            "sustainability": {
                "youTubeVideoId": null,
                "description": null,
                "highlights": []
            },
            "thirdPartyScripts": null,
            "title": "ageLOC Rose Gold LumiSpa® iO",
            "secondaryTitle": null,
            "usage": {
                "steps": [],
                "recommendations": [],
                "warnings": [],
                "additionalText": [],
                "youTubeVideoId": "",
                "markdown": null
            },
            "variantSelectLabel": null,
            "variants": [
                {
                    "availableChannels": [
                        "subscription",
                        "arsPhone",
                        "kiosk",
                        "mobile",
                        "web"
                    ],
                    "availableQuantity": 10,
                    "brandFamily": "ageLOC LumiSpa",
                    "channels": null,
                    "chargeShipping": true,
                    "customerTypes": [
                        "BrandAffiliate",
                        "Preferred",
                        "Retail"
                    ],
                    "dangerousGoods": false,
                    "description": "Where your skin care gets smarter and your results get even more amazing. ageLOC LumiSpa iO pairs an intelligent, one-of-a-kind device that uses patented technology with powerful products. The results? You get the skin of your dreams.",
                    "disclaimers": [],
                    "excludeFromSearch": false,
                    "foreignOrderLimit": 2,
                    "globalId": "GP001055",
                    "id": null,
                    "isExclusive": false,
                    "marketAttributes": {
                        "discount": false,
                        "redeem": false,
                        "earn": false
                    },
                    "matchingVariant": null,
                    "maxQuantity": 10,
                    "nettoWeight": null,
                    "orderType": null,
                    "points": {
                        "wholesale": {
                            "cv": 150,
                            "pv": 167,
                            "sb": null
                        },
                        "subscription": {
                            "cv": 150,
                            "pv": 167,
                            "sb": null
                        }
                    },
                    "totalPoints": null,
                    "price": {
                        "currencyCode": "USD",
                        "retail": 245,
                        "wholesale": 199,
                        "retailSales": null,
                        "wholesaleSales": null,
                        "retailSubscription": 245,
                        "wholesaleSubscription": 199
                    },
                    "totalPrice": null,
                    "pricingJson": "{\"prices\":[{\"type\":null,\"price\":245,\"currency\":\"USD\",\"currencySymbol\":null,\"minPrice\":null,\"maxPrice\":null,\"regularPrice\":null,\"priceFacets\":null}],\"totalValue\":{\"priceAfterDiscount\":245,\"originalPrice\":245,\"totaldiscount\":0,\"roundoff\":null,\"priceFacets\":{\"CV\":{\"CV\":150},\"Regular Price\":{\"Regular Price\":245},\"PV\":{\"PV\":167},\"Wholesale Price\":{\"Wholesale Price\":199}}}}",
                    "primaryBrand": "ageLOC LumiSpa",
                    "productType": null,
                    "purchaseTypes": {
                        "buyOnce": true,
                        "subscription": true
                    },
                    "restrictedMarkets": [],
                    "salesDisclaimer": "It’ s super intuitive. Super effective. Super-powered.",
                    "salesLabel": null,
                    "salesText": null,
                    "scanQualifiedCount": 0,
                    "searchKeywords": "ageloc, lumispa, io, vera, app, glow, regimen, skin, renewal, device, nu skin, pink",
                    "shadeable": false,
                    "size": null,
                    "sku": "01002594",
                    "slug": null,
                    "status": {
                        "status": "sellable",
                        "isBackordered": false,
                        "backorderedAvailableDate": null
                    },
                    "title": "ageLOC Rose Gold LumiSpa® iO",
                    "variantColor": null,
                    "variantLabel": null,
                    "benefits": {
                        "benefits": "*   Provides instant benefits, so skin feels softer and smoother after just one use.\n*   Seven clinically proven facial skin benefits with twice daily use: softness, smoothness, radiance, clarity, purified skin, reduced pore appearance, and visibly improved firmness.\n*   Benefits intensify over time when consistently used for two minutes twice daily.\n*   Delivers brighter, healthier, more youthful-looking skin in as little as two weeks.\n*   ageLOC treatment cleanser options are designed for different skin types: dry, normal to combination, oily, sensitive, and blemish prone.\n*   Optimally designed for LumiSpa iO, the treatment cleansers are proven to maximize the skin perfecting and cleansing benefits of the device.\n*   Treatment cleansers are formulated with Nu Skin’ s proprietary ageLOC ingredient blend to target the sources of aging and help preserve the look of youth.\n*   Gentle enough for twice-daily use on the face, neck, and décolleté.\n*   When used in the morning, LumiSpa iO energizes skin for a fresher, smoother, more rejuvenated looking complexion.\n*   When used at night, LumiSpa iO deeply cleanses and helps de-stress skin.",
                        "image": null,
                        "youTubeVideoId": ""
                    },
                    "disclaimerWarnings": null,
                    "faqs": null,
                    "features": null,
                    "ingredients": null,
                    "productDetails": {
                        "description": "Hello, iO. ageLOC LumiSpa iO inputs smart skin care and outputs the skin of your dreams. How? Input innovative skin renewal and deep cleansing with intelligent coaching, personalized regimens, IoT technology—and more—through the Nu Skin Vera® app. Output gorgeous, glowing, selfie-ready skin—all day, every day. In just two minutes, twice a day, you’ll experience your best skin ever. You’ll love your glow-boosting, instantly smoothed look—after just one use—the seven clinically proven skin benefits that amplify over time, and smart technology that helps you personalize your routine.",
                        "includedItems": [],
                        "highlights": [],
                        "originCountry": "",
                        "importer": "",
                        "warnings": ""
                    },
                    "productImages": [
                        {
                            "url": "https://nuskin.com/content/dam/global/library/mar2023/01002594-rose-gold-lumispa-io-2.jpg",
                            "alt": "",
                            "thumbnail": "https://nuskin.com/content/dam/global/library/mar2023/01002594-rose-gold-lumispa-io-2.jpg"
                        },
                        {
                            "url": "https://nuskin.com/content/dam/global/library/mar2023/01002594-rose-gold-lumispa-io-3.jpg",
                            "alt": "",
                            "thumbnail": "https://nuskin.com/content/dam/global/library/mar2023/01002594-rose-gold-lumispa-io-3.jpg"
                        },
                        {
                            "url": "https://nuskin.com/content/dam/global/library/mar2023/01002594-rose-gold-lumispa-io-1.jpg",
                            "alt": "",
                            "thumbnail": "https://nuskin.com/content/dam/global/library/mar2023/01002594-rose-gold-lumispa-io-1.jpg"
                        }
                    ],
                    "resources": [
                        {
                            "title": "ageLOC LumiSpa iO - Product Information Page",
                            "url": "https://nuskin.com/content/dam/office/n_america/US/en/nuskin_products/us-en-lumispa-io-pip.pdf"
                        }
                    ],
                    "results": {
                        "summary": [],
                        "results": [],
                        "report": {
                            "url": "",
                            "text": ""
                        },
                        "youTubeVideoId": ""
                    },
                    "usage": {
                        "steps": [],
                        "recommendations": [],
                        "warnings": [],
                        "additionalText": [
                            "Use ageLOC LumiSpa iO morning and night as your cleansing step. Moisten your face and then dispense an ample amount of cleanser onto your hand. Apply evenly to your face and then treat and cleanse with your LumiSpa iO device for two minutes or follow your custom routine with your preferred toner, serum, and moisturizer."
                        ],
                        "youTubeVideoId": "",
                        "markdown": null
                    }
                }
            ],
            "warranty": null,
            "bundle": null,
            "productDataSource": {
                "source": "equinox",
                "webBaseUrl": "https://test.nuskin.com/",
                "apiBaseUrl": "https://storefront.api.test.nuskin.com",
                "storeId": "430"
            },
            "crossProductIds": null,
            "upSellProductIds": null
        }
    }
}
"""



def run():
  st.set_page_config(
      page_title="Nu Skin LLM-Bot Prototype",
      page_icon="🤖",
  )

  st.title("Nu Skin LLM-Bot Prototype")

  openai.api_key = st.secrets["OPENAI_API_KEY"]

  if "openai_model" not in st.session_state:
      st.session_state["openai_model"] = "gpt-4"

  if "messages" not in st.session_state:
      st.session_state.messages = [
          {"role": "system", "content": SYSTEM_PROMPT},
          {"role": "assistant", "content": "Welcome to Nu Skin. How can I help you?"}
        ]

  for message in st.session_state.messages:
      if message["role"] == "user" or message["role"] == "assistant":
        with st.chat_message(message["role"]):
              st.markdown(message["content"])

  if prompt := st.chat_input("Enter text here"):
      st.session_state.messages.append({"role": "user", "content": prompt})
      with st.chat_message("user"):
          st.markdown(prompt)

      with st.chat_message("assistant"):
          message_placeholder = st.empty()
          full_response = ""
          for response in openai.ChatCompletion.create(
              model=st.session_state["openai_model"],
              messages=[
                  {"role": m["role"], "content": m["content"]}
                  for m in st.session_state.messages
              ],
              stream=True,
          ):
              full_response += response.choices[0].delta.get("content", "")
              message_placeholder.markdown(full_response + "▌")
          message_placeholder.markdown(full_response)
      st.session_state.messages.append({"role": "assistant", "content": full_response})


if __name__ == "__main__":
    run()
