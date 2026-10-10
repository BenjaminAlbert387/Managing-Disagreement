# Character definition
define y = Character("You")
define b = Character("Person B")
define c = Character("Person C")

# HUD display
default listening_score = 0
default inclusion_score = 0
default resolution_score = 0

screen confidence_ui():
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 5

        frame:
            text "Active Listening Score (Considers opposing viewpoints before making a judgement): [listening_score]"

        frame:
            text "Inclusion Score (Creates space for quieter staff members to contribute.): [inclusion_score]"

        frame:
            text "Resolution Score (Moves discussion towards a respectful, workable decision): [resolution_score]"

label start:

    show screen confidence_ui

    "Welcome! To continue, please press left click on your mouse / tap your mousepad while your cursor is on the game."

    "Great! This is a simulated scenario based on Managing Disagreement."

    "Please note that this is a fictional video game, and there are no real names used."

    "During the game, you will have the option to 'choose your response' through key points."

    "There are no right or wrong answers, and many options will increase one or more scores while lowering others. That is life!"

    "Once you are ready, press left click one more time and the simulated scenario will start!"

    # Scenario Start

    "Managing Disagreement: Scenario Start"

    
label scenario_two:

    scene black
    with fade

    "Wednesday, 6:05 PM. Trustee meeting."

    "The meeting has been going for forty minutes. There are half-empty mugs on the table, a spreadsheet projected onto the wall, and a growing sense that nobody is going home on time."

    "The Trustees are discussing a proposed charity initiative. It could help more people access the charity's services, but it would require additional funding and volunteer hours."

    b "I think we should approve the initiative. We've spent months talking about reaching more people, and this is an opportunity to actually do something."

    b "We have a workable proposal, we've identified potential funding, and we shouldn't let the fear of taking a risk stop us from making progress."

    "Another Trustee begins to respond, but Person B continues before they can finish."

    b "I know there are concerns about the workload, but we can't keep delaying everything because there might be complications."

    y "{i}Here we go. We've reached the stage of the meeting where everyone has an opinion, nobody has enough time, and the spreadsheet is somehow the least confusing thing in the room.{/i}"

    y "{i}Person B has a point. The initiative could make a genuine difference. But I can see that some of the other Trustees aren't comfortable with how quickly we're moving.{/i}"

    "Across the table, another Trustee, Person C, looks down at their notes. They have been trying to contribute for the past ten minutes, but every attempt has been interrupted."

    "You notice Person C close their notebook."

    y "{i}That's not a great sign. They might have decided they have nothing useful to add, or they might simply be tired. Either way, we risk making a decision without hearing everyone who has something to contribute.{/i}"

    b "Honestly, I think we're overcomplicating this. If we keep discussing every possible problem, we'll never get anything done."

    y "{i}I disagree with that approach, but I also don't want to turn this into a personal argument. Person B is clearly invested in the proposal. If I challenge them badly, the discussion could become about defending positions instead of solving the problem.{/i}"

    b "What do you think? Should we just vote and move on?"

    menu:
        "How do you respond to Person B?":

            "Agree to vote immediately so the meeting can move forward.":
                $ active_listening_score -= 1
                $ inclusion_score -= 2
                $ resolution_score += 0

                y "I think we should vote. We've discussed this enough, and we need to make a decision."

                b "Exactly. Thank you."

                "A vote is called. Several Trustees raise their hands, but Person C does not."

                y "{i}We've reached a decision quickly, but speed isn't the same as good decision-making. We haven't established whether the concerns have been properly understood.{/i}"

                y "{i}A majority vote can settle a disagreement. It doesn't automatically mean we've made the best decision we could have made.{/i}"

            "Pause the discussion and invite the quieter Trustees to speak.":
                $ active_listening_score += 2
                $ inclusion_score += 2
                $ resolution_score += 1

                y "Before we vote, I think we should hear from the people who haven't had much opportunity to contribute."

                y "Person B, I can see why you want us to make progress. Could we take a moment to understand the remaining concerns before deciding?"

                b "Fine. I just don't want us to spend another hour going in circles."

                y "Neither do I. Let's focus on the specific issues that could affect the decision."

                "You turn towards Person C."

                y "You looked like you wanted to add something earlier. Would you like to share your thoughts?"

                b "Go ahead."

                y "{i}I'm not trying to give one person more influence than another. I'm trying to make sure everyone has a fair opportunity to contribute before we decide.{/i}"

            "Tell Person B that they are dominating the meeting.":
                $ active_listening_score += 0
                $ inclusion_score += 1
                $ resolution_score -= 1

                y "Person B, you're dominating the conversation. We need to let other people speak."

                b "I'm trying to get us to make a decision. Someone has to keep things moving."

                y "I know, but you're interrupting people."

                "Person B leans back in their chair."

                b "Fine. I'll stop talking, then."

                y "{i}The issue needed addressing, but now Person B feels personally criticised. I've made it harder to have a constructive conversation.{/i}"

                y "{i}Sometimes a valid point can be delivered in a way that makes it less likely to be heard.{/i}"

    "A few moments pass."

    b "All right. What exactly are the concerns?"

    "Person C looks up from their notebook."

    b "I'm listening."

    "Person C hesitates before speaking."

    b "Go on. We haven't got all evening."

    y "{i}That last sentence probably wasn't helpful. Person C has finally started speaking, and now there's pressure to finish quickly.{/i}"

    "Person C takes a breath."

    c "I'm not against the initiative. I think it could help people. But I've looked at the volunteer rota, and we're already struggling to cover our existing services."

    c "If we launch something new without addressing that, we could end up reducing the quality of the support we're already providing."

    b "But we discussed volunteer recruitment last month. Surely we can recruit more people if we need to?"

    c "Possibly, but recruitment takes time. We don't have enough people available right now."

    b "We can't wait until every possible problem has been solved."

    y "{i}Both sides are raising legitimate points. Person B is worried about losing an opportunity. Person C is worried about overpromising and letting people down.{/i}"

    y "{i}The temptation is to pick a side. That would be easier than working through the actual disagreement, but it probably wouldn't help the charity make a better decision.{/i}"

    y "Could we separate the question of whether the initiative is worthwhile from the question of whether we're ready to launch it?"

    b "What do you mean?"

    y "We could agree that the initiative is worth pursuing, while still checking what staffing we need before committing to a launch date."

    "Person C nods."

    c "That would address my main concern. I don't want us to abandon the idea. I want us to make sure we can deliver it properly."

    b "I can see that. I just don't want us to keep postponing it indefinitely."

    y "{i}That's progress. We're no longer arguing about whether someone is being too cautious or too ambitious. We're starting to identify what each person actually needs from the decision.{/i}"

    b "So what do we do next?"

    menu:
        "How do you move the discussion forward?":

        "Suggest that the initiative be rejected because the risks are too high.":
                $ active_listening_score += 0
                $ inclusion_score += 0
                $ resolution_score += -2

                y "Given the staffing concerns, I think we should reject the proposal for now."

                b "We're just going to abandon it, then?"

                y "I don't think we have enough capacity."

                "Person C looks relieved, but Person B looks frustrated."

                y "{i}I've addressed one concern by effectively dismissing the other. We haven't explored whether a smaller launch or a revised timeline could work.{/i}"

                y "{i}A disagreement doesn't always need a compromise, but we should understand the alternatives before closing the discussion.{/i}"

        "Propose a smaller pilot with clear staffing requirements and a review date.":
                $ active_listening_score += 1
                $ inclusion_score += 2
                $ resolution_score += 2

                y "What if we start with a smaller pilot instead of launching the full initiative immediately?"

                y "We could identify the minimum number of volunteers needed, check whether we can meet that requirement, and agree on a date to review our readiness."

                b "That would let us make progress without committing to something we can't deliver."

                c "I'd support that, provided we don't use the pilot as a reason to stretch the existing team even further."

                y "Agreed. We should make the staffing requirement a condition, not just a recommendation."

                b "All right. I can work with that."

                y "{i}We've found a possible way forward by taking both concerns seriously. Nobody has got everything they originally wanted, but we have a plan that addresses the actual risks.{/i}"

            "Tell Person B and Person C to settle it between themselves.":
                $ active_listening_score += -1
                $ inclusion_score += -1
                $ resolution_score += -1

                y "You both have valid points. Why don't you discuss it between yourselves and come back with a decision?"

                b "We're discussing it now."

                c "I don't think it's just between us. The decision affects the whole charity."

                y "{i}I've delegated the disagreement without providing a way to resolve it. The rest of the Trustees are affected, and this is a collective decision.{/i}"

                y "{i}Calling something a conflict between two people doesn't make the underlying organisational problem disappear.{/i}"

    "The meeting continues."

    "The Trustees begin listing what would need to be confirmed before the initiative could proceed. The discussion becomes more practical, although not everyone agrees on every detail."

    b "I still think we could be moving faster."

    c "And I still think we need to be careful about what we promise."

    y "{i}They're still disagreeing. That doesn't necessarily mean we've failed.{/i}"

    y "{i}The goal of an inclusive discussion isn't to make everyone agree with one another. It's to make sure people can express concerns, understand the trade-offs, and contribute to a decision they can work with.{/i}"

    b "Can we at least agree on who is going to check the volunteer numbers and when we'll review the proposal?"

    y "Yes. Let's record the actions, assign owners, and set a date for reviewing the evidence."

    "The Trustees agree to check volunteer capacity before confirming the launch. Person B will update the proposal, Person C will help review the staffing requirements, and the board will revisit the decision at its next meeting."

    b "I can live with that. I still want to see this happen, though."

    y "I think we all do. We just need to make sure we're able to deliver what we promise."

    "The meeting finally ends."

    b "That took longer than I expected."

    y "At least we didn't spend another twenty minutes arguing about whether we were spending too long arguing."

    b "Give us time. We might add that to the agenda next week."

    "As the other Trustees begin packing up, Person B approaches you."

    b "Can I be honest? I felt like everyone was against my proposal tonight."

    b "I spent ages putting it together, and it felt like the moment I suggested moving forward, everyone focused on what could go wrong."

    y "{i}I wasn't expecting this conversation. We managed to agree on next steps, but Person B clearly hasn't left the meeting feeling heard.{/i}"

    y "{i}I could defend the decision, dismiss their frustration, or take the opportunity to understand what went wrong. The meeting is over, but the working relationship still matters.{/i}"

    menu:
        "How do you respond to Person B?":

        "Explain that the Trustees were right to challenge the proposal.":
                $ active_listening_score += -1
                $ inclusion_score += -1
                $ resolution_score += 0

                y "The concerns were legitimate. We couldn't just approve the proposal without checking the risks."

                b "I know that. I'm not saying we should have ignored them."

                b "I just wish people had acknowledged the work I'd put into it."

                y "{i}I've defended the decision without addressing what Person B was actually trying to tell me.{/i}"

        "Acknowledge their effort and ask what would have helped them feel heard.":
                $ active_listening_score += 2
                $ inclusion_score += 2
                $ resolution_score += 1

                y "I can see you've put a lot of work into this, and I don't think that effort was recognised enough tonight."

                y "Can you tell me what felt most frustrating about the discussion?"

                b "I felt like people had already decided it wouldn't work before I'd finished explaining it."

                y "That's worth reflecting on. We needed to examine the risks, but we also needed to give your proposal a fair hearing."

                b "Exactly. I'm happy to work through the concerns. I just don't want the initiative dismissed before we've properly considered it."

                y "That's fair. I'll raise how we structure these discussions at our next meeting, so we can challenge ideas without making people feel their contributions aren't valued."

                y "{i}Empathy doesn't mean agreeing with Person B's proposal. It means recognising their experience and considering whether our process could have been better.{/i}"

        "Tell them not to take disagreement personally.":
                $ active_listening_score += -1
                $ inclusion_score += 0
                $ resolution_score += -1

                y "It's a Trustee meeting. People are going to disagree with you sometimes."

                b "I know. That doesn't mean it felt constructive."

                y "{i}I've treated their concern as an overreaction instead of considering whether the way we handled the discussion contributed to it.{/i}"

    y "{i}A decision can be reasonable and still leave someone feeling unheard. Human-centred leadership means paying attention to both the outcome and how people are treated along the way.{/i}"

    y "{i}The decision isn't perfect, and the disagreement hasn't vanished. But people have been heard, the risks are clearer, and we have a practical next step.{/i}"

    y "{i}As a Trustee, I don't need to win every argument or make everyone happy. I need to help create the conditions for thoughtful decisions, even when people have different priorities.{/i}"

    y "{i}And ideally, I need to do that before the biscuits run out. Some conflicts are beyond even the most experienced leadership team.{/i}"

