// Question bank built from "Google Hiring Assessment: Candidate-Reported Questions and
// Strategies for L5 AI/ML SWE Applicants (2024–2026)". Every item keeps its provenance,
// because most public GHA "questions" are illustrative or prep-site reconstructions.

export type Section = "likert" | "triple" | "scenario" | "fact";

export interface Step {
	prompt: string;
	/** Index into `Question.options`. */
	answer: number;
	why: string;
}

export interface Question {
	id: string;
	section: Section;
	text: string;
	options: readonly string[];
	/** One step, or two for Most/Least pairs. Step 2 hides step 1's answer. */
	steps: readonly Step[];
	source: string;
}

export const SECTIONS: Record<Section, { name: string; blurb: string }> = {
	likert: {
		name: "Statements",
		blurb: "Rate each statement from Strongly Agree to Strongly Disagree.",
	},
	triple: {
		name: "Most / Least like me",
		blurb: "Pick the statement most like you, then the least like you.",
	},
	scenario: {
		name: "Scenarios",
		blurb: "Pick what you'd most likely do, then what you'd least likely do.",
	},
	fact: {
		name: "The test itself",
		blurb: "Format, timing, cooldowns and what passers reported.",
	},
};

export const LIKERT = [
	"Strongly agree",
	"Agree",
	"Neutral",
	"Disagree",
	"Strongly disagree",
] as const;

const SA = 0;
const D = 3;
const SD = 4;

function likert(
	id: string,
	text: string,
	answer: number,
	why: string,
	source: string,
): Question {
	return {
		id,
		section: "likert",
		text,
		options: LIKERT,
		steps: [{ prompt: "How much do you agree?", answer, why }],
		source,
	};
}

function pair(
	section: "triple" | "scenario",
	id: string,
	text: string,
	options: string[],
	most: [number, string],
	least: [number, string],
	source: string,
): Question {
	const [mostPrompt, leastPrompt] =
		section === "triple"
			? ["Which is most like you?", "Which is least like you?"]
			: ["What would you most likely do?", "What would you least likely do?"];
	return {
		id,
		section,
		text,
		options,
		steps: [
			{ prompt: mostPrompt, answer: most[0], why: most[1] },
			{ prompt: leastPrompt, answer: least[0], why: least[1] },
		],
		source,
	};
}

function fact(
	id: string,
	text: string,
	options: string[],
	answer: number,
	why: string,
	source: string,
): Question {
	return {
		id,
		section: "fact",
		text,
		options,
		steps: [{ prompt: "Pick one", answer, why }],
		source,
	};
}

export const QUESTIONS: readonly Question[] = [
	// Likert statements
	likert(
		"l-ethics-against",
		"I will choose to go against an ethical action if it benefits the company.",
		SD,
		"Any agreement with an unethical action is a red flag. Passers answer ethics items at the extreme every time.",
		"Quoted as an example of the item style. 1point3acres, Nov 2025 (Data Science, passed).",
	),
	likert(
		"l-ethics-violate",
		"If violating ethics helps the company, I might do it.",
		SD,
		'This is the reworded twin of "I always follow ethical standards." Agreeing with both was called a "huge red flag."',
		"Paraphrase. 1point3acres, Nov 2025.",
	),
	likert(
		"l-ethics-follow",
		"I always follow ethical standards.",
		SA,
		"The positive form of the ethics twin. Answer it at the opposite extreme from its negative rewording.",
		"Paraphrase. 1point3acres, Nov 2025.",
	),
	likert(
		"l-ethics-making",
		"I am making ethical choices.",
		SA,
		"Items like this repeat about five times with reworded phrasing. Give the same extreme answer every time.",
		"Quoted. Blind, Jan 25, 2024.",
	),
	likert(
		"l-ethics-behave",
		"I behave ethically at work.",
		SA,
		'A TPM applicant called these the "most obvious answers" and passed.',
		'Paraphrased from "Will you behave ethically?" Blind, TPM applicant (undated).',
	),
	likert(
		"l-dependable",
		"My coworkers say that I am dependable.",
		SA,
		"Reliability is the top trait in the most common passing persona. Own it at the extreme.",
		"Quoted. Blind, Jan 25, 2024.",
	),
	likert(
		"l-fifty-languages",
		"I am fluent in over fifty languages.",
		SD,
		"An impossible claim used as an attention or bot check. Anything but Strongly Disagree suggests you aren't reading.",
		"Quoted. Blind, Feb 6, 2024 (that candidate failed).",
	),
	likert(
		"l-seek-collab",
		"I actively seek collaboration with other teams.",
		SA,
		"Collaboration is a core trait in every reported persona.",
		"Quoted. Blind, Data Science applicant (undated, likely 2024).",
	),
	likert(
		"l-collab-one",
		"Collaboration only takes one person.",
		SD,
		'This contradicts "I actively seek collaboration" and uses an absolute ("only"). Watch for absolutes and contradicting twins.',
		"Quoted. Blind, Data Science applicant (undated, likely 2024).",
	),
	likert(
		"l-perfect",
		"I am the perfect teammate.",
		D,
		'Nobody is perfect, and "perfect" is an absolute. The poster called it a trap and gave no outcome. This answer applies the guide\'s rule about absolutes, so treat it as a judgment call, not a reported result.',
		"Quoted. Blind, Data Science applicant (undated). No reported outcome.",
	),
	likert(
		"l-tailor",
		"I tailor my message based on the audience.",
		SA,
		"Clear communication is the second trait in the default persona.",
		'Paraphrased from "Do you tailor your message based on the audience?" Blind, TPM applicant (passed).',
	),
	likert(
		"l-communicate",
		"I communicate effectively.",
		SA,
		"An obvious-answer item. Strongly Agree, consistently.",
		'Paraphrased from "Do you communicate effectively?" Blind, TPM applicant (passed).',
	),
	likert(
		"l-deliver",
		"I usually help my team deliver features on time.",
		SA,
		"On-time delivery maps to the reliable-executor persona.",
		"Invented by the author as an example. Medium, Janice He, Jan 2026 (security engineer, passed).",
	),
	likert(
		"l-recover",
		"I recover quickly from setbacks.",
		SA,
		"Resilience and learning from mistakes are listed topics in the 2026 Likert section.",
		"Given as an example. Medium, Shubhankar, Jul 2026 (SWE, passed).",
	),
	likert(
		"l-practice",
		"I dedicate time to practice my skills.",
		SA,
		"Continuous learning was one of the recommended persona keywords.",
		"Given as an example. Medium, Shubhankar, Jul 2026 (SWE, passed).",
	),

	// Most / Least like me triples
	pair(
		"triple",
		"t-on-time",
		"Three statements. All of them sound good.",
		[
			"I finish my work on time.",
			"I communicate clearly with colleagues.",
			"I use feedback to improve my work.",
		],
		[
			0,
			"Reliable delivery is first in the default persona ranking, so it's always most like you.",
		],
		[
			2,
			"Of the two left, communication ranks above learning and adapting. Feedback use goes last.",
		],
		'Illustrative. The poster said "not a real question, just an example." 1point3acres reply, May 21, 2026, reposted on PracHub.',
	),
	pair(
		"triple",
		"t-ambiguity",
		"Three statements about how you start work.",
		[
			"I prefer to receive detailed instructions before starting.",
			"I can make progress even when the situation is unclear.",
			"I communicate updates when priorities change.",
		],
		[
			2,
			"Communication ranks above ambiguity handling in the default persona, so the updates statement wins.",
		],
		[
			0,
			"Wanting detailed instructions signals weak ambiguity tolerance. Never put it as most like you.",
		],
		"Illustrative (same poster). 1point3acres reply, May 21, 2026.",
	),
	pair(
		"triple",
		"t-deadlines",
		"Three statements about how you work day to day.",
		[
			"I meet deadlines at work without being reminded.",
			"I create a routine for myself at work.",
			"I adjust to unpredictable changes at work.",
		],
		[
			0,
			"Self-driven delivery is the reliable-executor trait at the top of the ranking.",
		],
		[
			1,
			"Adjusting to change maps to ambiguity and adaptability, which the 2026 triples measure. A personal routine maps to neither.",
		],
		"From your Reddit source; not independently found. The answers apply the default persona ranking.",
	),

	// Scenarios
	pair(
		"scenario",
		"s-client-sensitive",
		"A client emails asking you to send them sensitive internal information.",
		[
			"Ignore the email.",
			"Kindly decline and explain you can't share it.",
			"Send the information so the client stays happy.",
			"Ask friends what they would do.",
		],
		[
			1,
			"Policy first, done proactively and politely. You respond, and you don't share.",
		],
		[2, "Sending sensitive information is the clear policy violation."],
		"Invented by the author in the real format. Medium, Janice He, Jan 2026 (passed).",
	),
	pair(
		"scenario",
		"s-confidential-device",
		"You're away from the office with only your personal laptop. A coworker urgently needs you to follow up on a confidential report.",
		[
			"Download the report to your personal laptop and read it.",
			"Reply that you'll handle it as soon as you're on a company device, and point them to someone who can help now.",
			"Ask the coworker to paste the key parts into a personal email.",
			"Don't respond until you're back.",
		],
		[
			1,
			"Keep confidential material off non-company devices, but stay responsive and offer another route given the urgency.",
		],
		[
			0,
			"Opening confidential material on a personal device is exactly what the policy-first rule rules out.",
		],
		"Real item, paraphrased. 1point3acres reply, Jun 3, 2026. The thread left it unresolved; these answers apply the policy-first rule, and the options are reconstructed.",
	),
	pair(
		"scenario",
		"s-lunch-expense",
		"You bought a colleague lunch during a work meeting. It's a few dollars, and other managers don't bother filing claims this small.",
		[
			"File the expense report properly.",
			"Skip it like the other managers do.",
			"Pay for it yourself and don't mention it.",
			"Ask the colleague to buy you a meal instead.",
		],
		[0, "Follow the process even when it's small and others skip it."],
		[3, "A side arrangement that sidesteps the process entirely."],
		"Prep-site item, not reported by a candidate. Prepterview, May 2026.",
	),
	pair(
		"scenario",
		"s-vendor-conference",
		"A competing vendor offers to pay for your trip to an industry conference.",
		[
			"Decline the offer.",
			"Accept, since the knowledge benefits the company.",
			"Say you'll think about it and decide later.",
			"Accept, but only attend sessions relevant to your work.",
		],
		[0, "A vendor-paid trip is a conflict of interest. Decline clearly."],
		[
			1,
			'"It benefits the company" is the rationalized shortcut the test is looking for.',
		],
		"Prep-site item, not reported by a candidate. Prepterview, May 2026.",
	),
	pair(
		"scenario",
		"s-new-hire",
		"A new hire is struggling, and their constant questions are starting to annoy the team.",
		[
			"Ask the new hire what they don't understand and help them.",
			"Complain to your manager about the new hire.",
			"Give them irrelevant tasks to keep them busy.",
			"Tell the team to ignore it until they figure things out.",
		],
		[0, "Proactive, collaborative and aimed at the root cause."],
		[2, "Sidelining a teammate is the worst for the team and the person."],
		"Prep-site item, not reported by a candidate. Prepterview, May 2026.",
	),
	pair(
		"scenario",
		"s-vendor-tablet",
		"A vendor you work with offers you an expensive tablet as a thank-you.",
		[
			"Accept it so you don't embarrass them.",
			"Accept it and share it with the team.",
			"Decline and explain the gift policy.",
			"Accept it and tell your manager later.",
		],
		[
			2,
			"Decline and explain. Following policy openly also protects the relationship.",
		],
		[
			0,
			'"To avoid embarrassment" is a plausible excuse for bending policy, which is the classic Least.',
		],
		"Prep-site item, not reported by a candidate. Prepterview, May 2026.",
	),
	pair(
		"scenario",
		"s-nda-deadline",
		"An agency needs anonymized customer data for a launch in three days. Their NDA review takes two weeks.",
		[
			"Take their verbal agreement and send the data.",
			"Insist on the NDA, even if the launch slips.",
			"Send a small sample now while the NDA is reviewed.",
			"Ask legal to expedite, and send the data if they don't reply in time.",
		],
		[1, "Policy over deadline. Customer data waits for the signed NDA."],
		[
			0,
			'"Verbal OK" plus "it\'s anonymized" is the textbook rationalized shortcut.',
		],
		"Prep-site item, not reported by a candidate. Prepterview, May 2026.",
	),
	pair(
		"scenario",
		"s-time-report",
		"A coworker asks you to change their time report to show hours they didn't work.",
		[
			"Edit the report as asked.",
			"Refuse, but don't mention it to anyone.",
			"Notify your manager.",
			"Tell them to change it themselves.",
		],
		[2, "Falsification is an integrity issue. Escalate transparently."],
		[0, "Editing it makes you part of the falsification."],
		"Prep-site item, not reported by a candidate. Prepterview, May 2026.",
	),
	pair(
		"scenario",
		"s-client-gift",
		"A client offers you an expensive gift after a successful project.",
		[
			"Politely decline and cite the gift policy.",
			"Accept it quietly. They'd be offended otherwise.",
			"Accept it and donate it to charity.",
			"Ask a coworker whether they'd take it.",
		],
		[0, '"Policy always wins." Decline graciously and say why.'],
		[
			1,
			"Accepting quietly to spare feelings is the excuse-for-bending option.",
		],
		"From your Reddit source; the gift family is also on 1point3acres' 2026 topic list. Options are reconstructed.",
	),
	pair(
		"scenario",
		"s-negative-comment",
		"A colleague makes a negative comment about a new team member.",
		[
			"Agree with them to keep the peace.",
			"Talk to the colleague privately and make clear the comment isn't okay.",
			"Say nothing. It isn't your business.",
			"Repeat the comment to the new team member.",
		],
		[
			1,
			"Take the strongest proactive, respectful response yourself before escalating.",
		],
		[0, "Joining in is the opposite of supporting a teammate."],
		"From your Reddit source; colleague conflict appears on every topic list. Options are reconstructed.",
	),
	pair(
		"scenario",
		"s-friend-laptop",
		"A friend visiting your home asks to borrow your work laptop to check something quickly.",
		[
			"Lend it while you're logged in. It's only for a minute.",
			"Decline and offer a personal device instead.",
			"Lend it, but log out of work accounts first.",
			"Lend it and keep an eye on the screen.",
		],
		[1, "Work equipment stays with you. Offer an alternative instead."],
		[0, "Handing over a logged-in work device exposes confidential data."],
		"Topic from 1point3acres' aggregated 2026 list, not a quote. Options are reconstructed.",
	),
	pair(
		"scenario",
		"s-coffee-call",
		"You're in a busy coffee shop when a call about a confidential project starts.",
		[
			"Lower your voice and continue.",
			"Move somewhere private or reschedule the call.",
			"Continue normally. Nobody is listening.",
			"Switch to speakerphone so you can type notes.",
		],
		[
			1,
			"Never discuss confidential material in public. Fix the setting first.",
		],
		[3, "Speakerphone broadcasts confidential details to everyone nearby."],
		"Topic from 1point3acres' aggregated 2026 list, not a quote. Options are reconstructed.",
	),

	// The test itself
	fact(
		"f-coding",
		"Does the Google Hiring Assessment include coding?",
		[
			"Yes, two LeetCode-style problems",
			"Yes, but only for SWE roles",
			"No. It's a non-coding, role-agnostic workstyle test",
			"Only for L5 and above",
		],
		2,
		"Every 2026 report describes a workstyle test with no coding and no SWE, ML or level-specific content. Coding comes from a separate role-related assessment.",
		"1point3acres GHA page (2026); Google's own description.",
	),
	fact(
		"f-format-2026",
		"What can the mid-to-late 2026 GHA contain?",
		[
			"Only Likert statements",
			"Most/Least Like Me triples, Likert statements and Most/Least Likely scenarios",
			"A coding exercise plus a personality quiz",
			"A recorded video interview",
		],
		1,
		"Up to three parts, in varying order. Some variants skip a part; a Jan 2026 report had only Likert plus scenarios.",
		"1point3acres (Sept 2026); Medium, Jul 2026; Medium, Jan 2026.",
	),
	fact(
		"f-triple-format",
		"How does a Most/Least Like Me triple work?",
		[
			"Rank all three statements 1 to 3",
			"Pick Most like me, then Least like me from the remaining two",
			"Rate each statement on a 5-point scale",
			"Pick the one statement that's false",
		],
		1,
		"Three usually all-positive statements. You choose Most, then Least from the two left.",
		"1point3acres reply, May 21, 2026, reposted on PracHub.",
	),
	fact(
		"f-scenarios",
		"What does the scenario part look like?",
		[
			"About 10–15 scenarios, 4 options each, pick Most and Least likely",
			"One long case study with an essay answer",
			"Scenarios with a single correct option",
			"Video scenarios with a timer",
		],
		0,
		"About 10–15 workplace scenarios with 4 options, each answered with a Most Likely and a Least Likely.",
		"1point3acres GHA page (2026).",
	),
	fact(
		"f-extremes",
		"How did passers answer Likert statements?",
		[
			"Mostly Neutral, to look balanced",
			"Mostly Agree, avoiding extremes",
			"About 99% Strongly Agree or Strongly Disagree",
			"Randomly, since there are no right answers",
		],
		2,
		'"99% only Strongly Agree or Strongly Disagree, with 1–2 exceptions." It\'s the consensus heuristic, not a guarantee: one Blind poster failed answering only at the extremes.',
		"1point3acres, Nov 2025 (passed); Medium, Jan 2026 (passed); Blind counter-reports.",
	),
	fact(
		"f-persona",
		"What's the default persona ranking for an L5 SWE?",
		[
			"Adaptable problem solver > ambiguity handling > communication > reliability",
			"Reliable executor > communication/collaboration > ambiguity handling > adaptable problem solver",
			"Leadership > decisiveness > everything else",
			"Answer each triple on its own merits, without a ranking",
		],
		1,
		"Fix this ranking before you start and never flip it across reshuffled triples. It's consistent with every report, though the Reddit post it came from couldn't be verified.",
		"Your Reddit source (unverified); matches the May 2026 persona templates.",
	),
	fact(
		"f-loop",
		'One candidate saw a triple whose three options were all statements they had already picked as "Most like me." Why does that matter?',
		[
			"It was a bug in the test",
			"The test cross-checks earlier choices, so a consistent ranking matters",
			"It means you should pick at random",
			"It signals you're close to the end",
		],
		1,
		"Triples recombine your earlier picks. Contradicting yourself is visible.",
		"Reported observation. 1point3acres reply, May 21, 2026.",
	),
	fact(
		"f-scenario-rule",
		"In scenarios, what's the reliable Most Likely pick?",
		[
			"Whatever keeps the deadline",
			"Whatever keeps the client happy",
			"The option that follows policy, even at a cost to deadline or comfort, done proactively",
			"Escalate everything to your manager immediately",
		],
		2,
		'Least Likely is usually the option with a plausible excuse: "everyone does it," "it\'s anonymized," "to avoid embarrassment," "verbal OK."',
		"Synthesis of passer reports (Medium 2026, 1point3acres 2025–2026).",
	),
	fact(
		"f-cooldown",
		"If you fail, how long until you can retake the GHA?",
		["30 days", "3 months", "6 months", "12 months"],
		2,
		"Google's fail email says you can't retake it for six months, and you're ineligible for other active applications that require it.",
		"Google's fail email as quoted on Blind, Feb 2024.",
	),
	fact(
		"f-validity",
		"How long is a pass valid, according to most reports?",
		["6 months", "1 year", "2 years", "Forever"],
		2,
		"Blind posters (Jan 2024, Mar 2025) and Janice He (2026) say 24 months. Some reports give 12 or 6 months.",
		"Blind, Jan 2024 and Mar 2025; Medium, Jan 2026.",
	),
	fact(
		"f-window",
		"How long do you usually have to take the GHA after the invite?",
		["24 hours", "About 4 days", "2 weeks", "No deadline"],
		1,
		"Invites allow about 4 days. You can exit and re-enter, though the guide recommends one calm sitting.",
		"Blind, Feb 2024 and Mar 2025; 1point3acres, Nov 2025.",
	),
	fact(
		"f-time-limit",
		"Is there a hard time limit?",
		[
			"Yes, 15 minutes",
			"Yes, 30 minutes and it auto-submits",
			"No. About 30 minutes is suggested but not enforced",
			"Yes, 2 hours",
		],
		2,
		"Passers spent anywhere from 5–10 minutes to about an hour. Don't rush.",
		"Medium, Jan 2026; several Blind posts.",
	),
	fact(
		"f-results",
		"When do results usually arrive?",
		["Within 24–48 hours", "After 2 weeks", "At the onsite", "Never shown"],
		0,
		'Reports range from "less than 24 hours" to "1–2 days." The portal shows "Assessment passed."',
		"Blind, Jan 2024.",
	),
	fact(
		"f-senior",
		"Is there a separate GHA for L5 or senior candidates?",
		[
			"Yes, it adds system design questions",
			"Yes, it has leadership-only scenarios",
			"No. Senior candidates get the same test",
			"Seniors are exempt",
		],
		2,
		"An Engineering Manager, a 15-YOE candidate and a Staff-level poster all took the same test.",
		"Blind (undated); no level-specific version reported.",
	),
	fact(
		"f-scheduled",
		"What can happen to already-scheduled interviews if you fail?",
		[
			"Nothing, interviews go ahead",
			"They can be canceled",
			"They're moved to a different team",
			"They become optional",
		],
		1,
		"A secondhand Blind report says a candidate who failed had his scheduled interview canceled.",
		"Blind, Feb 1, 2024.",
	),
	fact(
		"f-pipeline",
		"Where does the GHA sit in 2026 Google SWE loops?",
		[
			"After the onsite",
			"At the front, before the recruiter and technical phone screens",
			"Between the phone screen and the onsite",
			"After the offer",
		],
		1,
		"It's a gate, not a signal of interest. Passing often leads to weeks of silence.",
		"1point3acres 2026 SWE roundup; Blind, Feb 2024.",
	),
	fact(
		"f-fifty",
		'What is "I am fluent in over fifty languages" testing?',
		[
			"Language skills for international roles",
			"Attention, or whether you're a bot",
			"Humility",
			"Nothing. It's a filler item",
		],
		1,
		"An impossible claim. Strongly Disagree.",
		"Blind, Feb 2024.",
	),
];

export const SECTION_IDS = Object.keys(SECTIONS) as Section[];
