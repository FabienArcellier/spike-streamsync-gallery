import streamsync as ss

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://streamsync.cloud

def click_img(state, context):
    state["image"] = context['item']

initial_state = ss.init_state({
    "images": {
        "1": {
            "caption": "curiosity",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/PIA16239_High-Resolution_Self-Portrait_by_Curiosity_Rover_Arm_Camera_square.jpg/600px-PIA16239_High-Resolution_Self-Portrait_by_Curiosity_Rover_Arm_Camera_square.jpg"
        },
        "2": {
            "caption": "",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/MarsCuriosityRover-Drilling-Sol170%2B%2B-2.jpg/542px-MarsCuriosityRover-Drilling-Sol170%2B%2B-2.jpg",
        },
        "3": {
            "caption": "",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Mars_2020_selfie_containing_both_perseverance_rover_and_ingenuity.gif/800px-Mars_2020_selfie_containing_both_perseverance_rover_and_ingenuity.gif",
        },
        "4": {
            "caption": "",
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/PIA16226-MarsCuriosityRover-FirstScoopOfSoil-20121007.jpg/1920px-PIA16226-MarsCuriosityRover-FirstScoopOfSoil-20121007.jpg",
        }
    },
    "image": {
        "caption": "",
        "url": ""
    }
})

initial_state['image'] = initial_state['images']["1"]
initial_state.import_stylesheet('main', '/static/main.css')
