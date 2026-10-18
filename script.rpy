# Character definition
define y = Character("You")
define b = Character("Person B")
define c = Character("Person C")

# HUD display
default active_listening_score = 0
default inclusion_score = 0
default resolution_score = 0

screen confidence_ui():
    vbox:
        xalign 0.98
        yalign 0.02
        spacing 5

        frame:
            text "Active Listening Score (Considers opposing viewpoints before making a judgement): [active_listening_score]"

        frame:
            text "Inclusion Score (Creates space for quieter staff members to contribute.): [inclusion_score]"

        frame:
            text "Resolution Score (Moves discussion towards a respectful, workable decision): [resolution_score]"

label start:

    show screen confidence_ui

    play sound "voice_lines/1.mp3"
    "Welcome! To continue, please press left click on your mouse / tap your mousepad or screen while your cursor is on the game."
    
    play sound "voice_lines/2.mp3"
    "Great! This is a simulated scenario based on Managing Disagreement."

    play sound "voice_lines/3.mp3"
    "Please note that this is a fictional video game, and there are no real names used."

    play sound "voice_lines/4.mp3"
    "During the game, you will have the option to 'choose your response' through key points."

    play sound "voice_lines/5.mp3"
    "There are no right or wrong answers, and many options will increase one or more scores while lowering others. That is life!"

    play sound "voice_lines/6.mp3"
    "Once you are ready, press left click one more time and the simulated scenario will start!"

    # Scenario Start

    play sound "voice_lines/7.mp3"
    "Managing Disagreement: Scenario Start"

    
label scenario_two:

    scene black
    with fade

    play sound "voice_lines/8.mp3"
    "Wednesday, 6:05 PM. Trustee meeting."

    play sound "voice_lines/9.mp3"
    "The meeting has been going for forty minutes. There are half-empty mugs on the table, a spreadsheet projected onto the wall, and a growing sense that nobody is going home on time."

    play sound "voice_lines/10.mp3"
    "The Trustees are discussing a proposed charity initiative. It could help more people access the charity's services, but it would require additional funding and volunteer hours."

    play sound "voice_lines/11.mp3"
    b "I think we should approve the initiative. We've spent months talking about reaching more people, and this is an opportunity to actually do something."

    play sound "voice_lines/12.mp3"
    b "We have a workable proposal, we've identified potential funding, and we shouldn't let the fear of taking a risk stop us from making progress."

    play sound "voice_lines/13.mp3"
    "Another Trustee begins to respond, but Person B continues before they can finish."

    play sound "voice_lines/14.mp3"
    b "I know there are concerns about the workload, but we can't keep delaying everything because there might be complications."

    play sound "voice_lines/15.mp3"
    y "{i}Here we go. We've reached the stage of the meeting where everyone has an opinion, nobody has enough time, and the spreadsheet is somehow the least confusing thing in the room.{/i}"

    play sound "voice_lines/16.mp3"
    y "{i}Person B has a point. The initiative could make a genuine difference. But I can see that some of the other Trustees aren't comfortable with how quickly we're moving.{/i}"

    play sound "voice_lines/17.mp3"
    "Across the table, another Trustee, Person C, looks down at their notes. They have been trying to contribute for the past ten minutes, but every attempt has been interrupted."

    play sound "voice_lines/18.mp3"
    "You notice Person C close their notebook."

    play sound "voice_lines/19.mp3"
    y "{i}That's not a great sign. They might have decided they have nothing useful to add, or they might simply be tired. Either way, we risk making a decision without hearing everyone who has something to contribute.{/i}"

    play sound "voice_lines/20.mp3"
    b "Honestly, I think we're overcomplicating this. If we keep discussing every possible problem, we'll never get anything done."

    play sound "voice_lines/21.mp3"
    y "{i}I disagree with that approach, but I also don't want to turn this into a personal argument. Person B is clearly invested in the proposal. If I challenge them badly, the discussion could become about defending positions instead of solving the problem.{/i}"

    play sound "voice_lines/22.mp3"
    b "What do you think? Should we just vote and move on?"

    menu:
        "How do you respond to Person B?"

        "Agree to vote immediately so the meeting can move forward.":
                $ active_listening_score -= 1
                $ inclusion_score -= 2
                $ resolution_score += 0

                play sound "voice_lines/23.mp3"
                y "I think we should vote. We've discussed this enough, and we need to make a decision."

                play sound "voice_lines/24.mp3"
                b "Exactly. Thank you."

                play sound "voice_lines/25.mp3"
                "A vote is called. Several Trustees begin to raise their hands, but Person C does not."

                play sound "voice_lines/26.mp3"
                "Then, the trustees put their hands back down. It's clear they are second guessing the vote."

                play sound "voice_lines/27.mp3"
                y "{i}We've reached a decision quickly, but speed isn't the same as good decision-making. We haven't established whether the concerns have been properly understood.{/i}"

                play sound "voice_lines/28.mp3"
                y "{i}A majority vote can settle a disagreement. It doesn't automatically mean we've made the best decision we could have made.{/i}"

        "Pause the discussion and invite the quieter Trustees to speak.":
                $ active_listening_score += 2
                $ inclusion_score += 2
                $ resolution_score += 1

                play sound "voice_lines/29.mp3"
                y "Before we vote, I think we should hear from the people who haven't had much opportunity to contribute."

                play sound "voice_lines/30.mp3"
                y "Person B, I can see why you want us to make progress. Could we take a moment to understand the remaining concerns before deciding?"

                play sound "voice_lines/31.mp3"
                b "Fine. I just don't want us to spend another hour going in circles."

                play sound "voice_lines/32.mp3"
                y "Neither do I. Let's focus on the specific issues that could affect the decision."

                play sound "voice_lines/33.mp3"
                "You turn towards Person C."

                play sound "voice_lines/34.mp3"
                y "You looked like you wanted to add something earlier. Would you like to share your thoughts?"

                play sound "voice_lines/35.mp3"
                b "Go ahead."

                play sound "voice_lines/36.mp3"
                y "{i}I'm not trying to give one person more influence than another. I'm trying to make sure everyone has a fair opportunity to contribute before we decide.{/i}"

        "Tell Person B that they are dominating the meeting.":
                $ active_listening_score += 0
                $ inclusion_score += -1
                $ resolution_score += 1

                play sound "voice_lines/37.mp3"
                y "Person B, you're dominating the conversation. We need to let other people speak."

                play sound "voice_lines/38.mp3"
                b "I'm trying to get us to make a decision. Someone has to keep things moving."

                play sound "voice_lines/39.mp3"
                y "I know, but you're interrupting people."

                play sound "voice_lines/40.mp3"
                "Person B leans back in their chair."

                play sound "voice_lines/41.mp3"
                b "Fine. I'll stop talking, then."

                play sound "voice_lines/42.mp3"
                y "{i}The issue needed addressing, but now Person B feels personally criticised. I've made it harder to have a constructive conversation.{/i}"

                play sound "voice_lines/43.mp3"
                y "{i}Sometimes a valid point can be delivered in a way that makes it less likely to be heard.{/i}"

    play sound "voice_lines/44.mp3"
    "A few moments pass."

    play sound "voice_lines/45.mp3"
    b "All right. What exactly are the concerns?"

    play sound "voice_lines/46.mp3"
    "Person C looks up from their notebook."

    play sound "voice_lines/47.mp3"
    b "I'm listening."

    play sound "voice_lines/48.mp3"
    "Person C hesitates before speaking."

    play sound "voice_lines/49.mp3"
    b "Go on. We haven't got all evening."

    play sound "voice_lines/50.mp3"
    y "{i}That last sentence probably wasn't helpful. Person C has finally started speaking, and now there's pressure to finish quickly.{/i}"

    play sound "voice_lines/51.mp3"
    "Person C takes a breath."

    play sound "voice_lines/52.mp3"
    c "I'm not against the initiative. I think it could help people. But I've looked at the volunteer rota, and we're already struggling to cover our existing services."

    play sound "voice_lines/53.mp3"
    c "If we launch something new without addressing that, we could end up reducing the quality of the support we're already providing."

    play sound "voice_lines/54.mp3"
    b "But we discussed volunteer recruitment last month. Surely we can recruit more people if we need to?"

    play sound "voice_lines/55.mp3"
    c "Possibly, but recruitment takes time. We don't have enough people available right now."

    play sound "voice_lines/56.mp3"
    b "We can't wait until every possible problem has been solved."

    play sound "voice_lines/57.mp3"
    y "{i}Both sides are raising legitimate points. Person B is worried about losing an opportunity. Person C is worried about overpromising and letting people down.{/i}"

    play sound "voice_lines/58.mp3"
    y "{i}The temptation is to pick a side. That would be easier than working through the actual disagreement, but it probably wouldn't help the charity make a better decision.{/i}"

    play sound "voice_lines/59.mp3"
    y "Could we separate the question of whether the initiative is worthwhile from the question of whether we're ready to launch it?"

    play sound "voice_lines/60.mp3"
    b "What do you mean?"

    play sound "voice_lines/61.mp3"
    y "We could agree that the initiative is worth pursuing, while still checking what staffing we need before committing to a launch date."

    play sound "voice_lines/62.mp3"
    "Person C nods."

    play sound "voice_lines/63.mp3"
    c "That would address my main concern. I don't want us to abandon the idea. I want us to make sure we can deliver it properly."

    play sound "voice_lines/64.mp3"
    b "I can see that. I just don't want us to keep postponing it indefinitely."

    play sound "voice_lines/65.mp3"
    y "{i}That's progress. We're no longer arguing about whether someone is being too cautious or too ambitious. We're starting to identify what each person actually needs from the decision.{/i}"

    play sound "voice_lines/66.mp3"
    b "So what do we do next?"

    menu:
        "How do you move the discussion forward?"

        "Suggest that the initiative be rejected because the risks are too high.":
                $ active_listening_score += 0
                $ inclusion_score += 0
                $ resolution_score += -2

                play sound "voice_lines/67.mp3"
                y "Given the staffing concerns, I think we should reject the proposal for now."

                play sound "voice_lines/68.mp3"
                b "We're just going to abandon it, then?"

                play sound "voice_lines/69.mp3"
                y "I don't think we have enough capacity."

                play sound "voice_lines/70.mp3"
                "Person C looks relieved, but Person B looks frustrated."

                play sound "voice_lines/71.mp3"
                y "{i}I've addressed one concern by effectively dismissing the other. We haven't explored whether a smaller launch or a revised timeline could work.{/i}"

                play sound "voice_lines/72.mp3"
                y "{i}A disagreement doesn't always need a compromise, but we should understand the alternatives before closing the discussion.{/i}"

        "Propose a smaller pilot with clear staffing requirements and a review date.":
                $ active_listening_score += 1
                $ inclusion_score += 2
                $ resolution_score += 2

                play sound "voice_lines/73.mp3"
                y "What if we start with a smaller pilot instead of launching the full initiative immediately?"

                play sound "voice_lines/74.mp3"
                y "We could identify the minimum number of volunteers needed, check whether we can meet that requirement, and agree on a date to review our readiness."

                play sound "voice_lines/75.mp3"
                b "That would let us make progress without committing to something we can't deliver."

                play sound "voice_lines/76.mp3"
                c "I'd support that, provided we don't use the pilot as a reason to stretch the existing team even further."

                play sound "voice_lines/77.mp3"
                y "Agreed. We should make the staffing requirement a condition, not just a recommendation."

                play sound "voice_lines/78.mp3"
                b "All right. I can work with that."

                play sound "voice_lines/79.mp3"
                y "{i}We've found a possible way forward by taking both concerns seriously. Nobody has got everything they originally wanted, but we have a plan that addresses the actual risks.{/i}"

        "Tell Person B and Person C to settle it between themselves.":
                $ active_listening_score += -1
                $ inclusion_score += -1
                $ resolution_score += -1

                play sound "voice_lines/80.mp3"
                y "You both have valid points. Why don't you discuss it between yourselves and come back with a decision?"

                play sound "voice_lines/81.mp3"
                b "We're discussing it now."

                play sound "voice_lines/82.mp3"
                c "I don't think it's just between us. The decision affects the whole charity."

                play sound "voice_lines/83.mp3"
                y "{i}I've delegated the disagreement without providing a way to resolve it. The rest of the Trustees are affected, and this is a collective decision.{/i}"

                play sound "voice_lines/84.mp3"
                y "{i}Calling something a conflict between two people doesn't make the underlying organisational problem disappear.{/i}"

    play sound "voice_lines/85.mp3"
    "The meeting continues."

    play sound "voice_lines/86.mp3"
    "The Trustees begin listing what would need to be confirmed before the initiative could proceed. The discussion becomes more practical, although not everyone agrees on every detail."

    play sound "voice_lines/87.mp3"
    b "I still think we could be moving faster."

    play sound "voice_lines/88.mp3"
    c "And I still think we need to be careful about what we promise."

    play sound "voice_lines/89.mp3"
    y "{i}They're still disagreeing. That doesn't necessarily mean we've failed.{/i}"

    play sound "voice_lines/90.mp3"
    y "{i}The goal of an inclusive discussion isn't to make everyone agree with one another. It's to make sure people can express concerns, understand the trade-offs, and contribute to a decision they can work with.{/i}"

    play sound "voice_lines/91.mp3"
    b "Can we at least agree on who is going to check the volunteer numbers and when we'll review the proposal?"

    play sound "voice_lines/92.mp3"
    y "Yes. Let's record the actions, assign owners, and set a date for reviewing the evidence."

    play sound "voice_lines/93.mp3"
    "The Trustees agree to check volunteer capacity before confirming the launch. Person B will update the proposal, Person C will help review the staffing requirements, and the board will revisit the decision at its next meeting."

    play sound "voice_lines/94.mp3"
    b "I can live with that. I still want to see this happen, though."

    play sound "voice_lines/95.mp3"
    y "I think we all do. We just need to make sure we're able to deliver what we promise."

    play sound "voice_lines/96.mp3"
    "The meeting finally ends."

    play sound "voice_lines/97.mp3"
    b "That took longer than I expected."

    play sound "voice_lines/98.mp3"
    y "At least we didn't spend another twenty minutes arguing about whether we were spending too long arguing."

    play sound "voice_lines/99.mp3"
    b "Give us time. We might add that to the agenda next week."

    play sound "voice_lines/100.mp3"
    "As the other Trustees begin packing up, Person B approaches you."

    play sound "voice_lines/101.mp3"
    b "Can I be honest? I felt like everyone was against my proposal tonight."

    play sound "voice_lines/102.mp3"
    b "I spent ages putting it together, and it felt like the moment I suggested moving forward, everyone focused on what could go wrong."

    play sound "voice_lines/103.mp3"
    y "{i}I wasn't expecting this conversation. We managed to agree on next steps, but Person B clearly hasn't left the meeting feeling heard.{/i}"

    play sound "voice_lines/104.mp3"
    y "{i}I could defend the decision, dismiss their frustration, or take the opportunity to understand what went wrong. The meeting is over, but the working relationship still matters.{/i}"

    menu:
        "How do you respond to Person B?"

        "Explain that the Trustees were right to challenge the proposal.":
                $ active_listening_score += -1
                $ inclusion_score += -1
                $ resolution_score += 0

                play sound "voice_lines/105.mp3"
                y "The concerns were legitimate. We couldn't just approve the proposal without checking the risks."

                play sound "voice_lines/106.mp3"
                b "I know that. I'm not saying we should have ignored them."

                #play sound "voice_lines/107.mp3"
                b "I just wish people had acknowledged the work I'd put into it."

                #play sound "voice_lines/108.mp3"
                y "{i}I've defended the decision without addressing what Person B was actually trying to tell me.{/i}"

        "Acknowledge their effort and ask what would have helped them feel heard.":
                $ active_listening_score += 2
                $ inclusion_score += 2
                $ resolution_score += 1

                #play sound "voice_lines/109.mp3"
                y "I can see you've put a lot of work into this, and I don't think that effort was recognised enough tonight."

                #play sound "voice_lines/110.mp3"
                y "Can you tell me what felt most frustrating about the discussion?"

                #play sound "voice_lines/111.mp3"
                b "I felt like people had already decided it wouldn't work before I'd finished explaining it."

                #play sound "voice_lines/112.mp3"
                y "That's worth reflecting on. We needed to examine the risks, but we also needed to give your proposal a fair hearing."

                #play sound "voice_lines/113.mp3"
                b "Exactly. I'm happy to work through the concerns. I just don't want the initiative dismissed before we've properly considered it."

                #play sound "voice_lines/114.mp3"
                y "That's fair. I'll raise how we structure these discussions at our next meeting, so we can challenge ideas without making people feel their contributions aren't valued."

                #play sound "voice_lines/115.mp3"
                y "{i}Empathy doesn't mean agreeing with Person B's proposal. It means recognising their experience and considering whether our process could have been better.{/i}"

        "Tell them not to take disagreement personally.":
                $ active_listening_score += -1
                $ inclusion_score += 0
                $ resolution_score += -1

                #play sound "voice_lines/116.mp3"
                y "It's a Trustee meeting. People are going to disagree with you sometimes."

                play sound "voice_lines/117.mp3"
                b "I know. That doesn't mean it felt constructive."

                #play sound "voice_lines/118.mp3"
                y "{i}I've treated their concern as an overreaction instead of considering whether the way we handled the discussion contributed to it.{/i}"

    play sound "voice_lines/119.mp3"
    y "{i}A decision can be reasonable and still leave someone feeling unheard. Human-centred leadership means paying attention to both the outcome and how people are treated along the way.{/i}"

    play sound "voice_lines/120.mp3"
    y "{i}The decision isn't perfect, and the disagreement hasn't vanished. But people have been heard, the risks are clearer, and we have a practical next step.{/i}"

    # Personal ending

    if active_listening_score < 0:

        play sound "voice_lines/121.mp3"
        "You may have focused more on defending a position or responding to disagreement than fully understanding the other person's perspective."

        play sound "voice_lines/122.mp3"
        "This can leave people feeling dismissed and make conflict harder to resolve."

        play sound "voice_lines/123.mp3"
        "Advice: Give others time to explain their concerns without interruption."

        play sound "voice_lines/124.mp3"
        "Ask clarifying questions, acknowledge their feelings, and summarise their position before offering your own response."

    elif active_listening_score == 0:
        
        play sound "voice_lines/125.mp3"
        "You may have considered some perspectives while overlooking others or moved towards solutions before fully understanding the disagreement."

        play sound "voice_lines/126.mp3"
        "Advice: Practise listening to understand rather than simply preparing your next response."

        #play sound "voice_lines/127.mp3"
        "Ask yourself whether you could accurately explain the other person's viewpoint before deciding how to proceed."

    else:

        #play sound "voice_lines/128.mp3"
        "Your decisions suggest that you made an effort to understand other perspectives and engage constructively with disagreement."

        #play sound "voice_lines/129.mp3"
        "Advice: Continue asking open questions, acknowledging concerns and checking your understanding."

        #play sound "voice_lines/130.mp3"
        "As a trustee, remember that listening to a viewpoint does not mean you must agree with it."

    if inclusion_score < 0:

        #play sound "voice_lines/131.mp3"
        "Your decisions suggest that some voices or perspectives may not have been adequately included in the discussion."

        #play sound "voice_lines/132.mp3"
        "When people feel excluded, the board risks overlooking important information and reinforcing existing power imbalances."

        #play sound "voice_lines/133.mp3"
        "Advice: Make a deliberate effort to invite contributions from everyone, particularly those who are quieter or less confident."

        #play sound "voice_lines/134.mp3"
        "Consider whose perspectives are missing and whether the meeting environment makes it easy for people to speak honestly."

    elif inclusion_score == 0:
        
        #play sound "voice_lines/135.mp3"
        "You demonstrated some awareness of inclusion, but there may have been missed opportunities to ensure that everyone could contribute meaningfully."

        #play sound "voice_lines/136.mp3"
        "Advice: Check whose contributions are influencing the discussion and whose are being overlooked."

        #play sound "voice_lines/137.mp3"
        "Encourage different viewpoints and explain how contributions have informed the final decision."

    else:
        
        #play sound "voice_lines/138.mp3"
        "Your decisions suggest that you valued different perspectives and recognised the importance of giving people a meaningful opportunity to participate."

        #play sound "voice_lines/139.mp3"
        "Advice: Continue creating space for different viewpoints, especially when there is a strong consensus or a more senior voice dominates."

        #play sound "voice_lines/140.mp3"
        "Make sure that disagreement can be expressed respectfully without people fearing that they will be dismissed."

    if resolution_score < 0:

        #play sound "voice_lines/141.mp3"
        "Your decisions suggest that the disagreement may not have been addressed constructively."

        #play sound "voice_lines/142.mp3"
        "Avoiding difficult issues, escalating tensions or pushing towards an outcome without addressing concerns can undermine trust and leave problems unresolved."

        #play sound "voice_lines/143.mp3"
        "Focus on the issue rather than the individuals involved. Identify the underlying concerns and look for shared objectives."

        #play sound "voice_lines/144.mp3"
        "If an immediate agreement is not possible, clarify what further discussion or information is needed."

    elif resolution_score == 0:

        #play sound "voice_lines/145.mp3"
        "You may have made some progress towards resolving the disagreement, but important concerns or next steps could remain unclear."

        #play sound "voice_lines/146.mp3"
        "Advice: Summarise the points of agreement and disagreement. Clarify the decision and explain the reasoning behind it."

        #play sound "voice_lines/147.mp3"
        "Remember that a constructive outcome does not require everyone to hold the same opinion."

    else:
        #play sound "voice_lines/148.mp3"
        "Your decisions suggest that you approached disagreement in a way that helped move the group towards a constructive outcome."

        #play sound "voice_lines/149.mp3"
        "Advice: Continue seeking solutions that address the underlying issues rather than simply ending the disagreement."

        #play sound "voice_lines/150.mp3"
        "Make sure decisions, responsibilities and follow-up actions are clear, and check that unresolved concerns are not being ignored."       

    #play sound "voice_lines/151.mp3"
    y "{i}As a Trustee, I don't need to win every argument or make everyone happy. I need to help create the conditions for thoughtful decisions.{/i}"

    #play sound "voice_lines/152.mp3"
    y "{i}And ideally, I need to do that before the biscuits run out. Some conflicts are beyond even the most experienced leadership team.{/i}"

    #play sound "voice_lines/153.mp3"
    "Simulated Scenario Finished! Press left click on your mouse / tap your mousepad or screen to return to the menu."