# ResearchKit

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/researchkit

# ResearchKit

研究アプリを使えば、ユーザが重要な医学研究にどこからでも参加することができます。

![ResearchKitアイコンのスケッチ。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせる青色になっています。](https://docs-assets.developer.apple.com/published/b46ac5aed3f686ad6f8d22976e7393c2/technologies-ResearchKit-intro%402x.png)

ResearchKitは、魅力的なカスタム研究アプリを簡単にデザインして構築することができる各種画面とトランジションがあらかじめ用意されたフレームワークです。デベロッパ向けのガイダンスは、[Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/)を参照してください。

以下のガイドラインは情報提供を目的としたものであり、法的なアドバイスではありません。研究アプリの開発および適用法に関するアドバイスについては、弁護士にお問い合わせください。

## [オンボーディング画面の作成](/jp/design/human-interface-guidelines/researchkit#Creating-the-onboarding-experience)

研究アプリの初回起動時には、調査の概要説明の画面、参加資格の確認の画面、調査の実施のための許可リクエストの画面のほか、必要な場合には個人データへのアクセス許可を求める画面も表示されます。これらの画面は一度確認が完了したら、あとで見返す類のものではないので、明瞭であることが不可欠です。

**オンボーディング画面は常に正しい順序で表示する。**

![ボックスが横1列に並んだ図。左のボックスから順に、右向き矢印で隣のボックスへとつながっています。ボックスのラベルは左から順に「起動画面」、「参加資格」、「インフォームドコンセント」、「データへのアクセス許可」です。](https://docs-assets.developer.apple.com/published/8035596669e5973efd8db1f6b5b29dc5/researchkit-diagram%402x.png)

### [1.起動画面](/jp/design/human-interface-guidelines/researchkit#1-Introduction)

**概要を伝え、アクションを呼びかける起動画面を用意する。** 調査のテーマと目的をはっきりと説明します。また、すでにオンボーディングを済ませているユーザが素早くログインして進行中の調査に戻るための手段も提供してください。

![iPhoneに表示されたResearchKitアプリの起動画面のスクリーンショット。ユーザに調査への参加を呼びかけています。](https://docs-assets.developer.apple.com/published/6d54dd639a4fe80b986ffb2ba12ba5e3/introduction-screen%402x.png)

### [2.参加資格の確認](/jp/design/human-interface-guidelines/researchkit#2-Determine-eligibility)

**できる限り早い段階で参加資格を確認する。** 調査への参加資格を満たしていないユーザが同意セクションに進む必要はありません。参加資格は調査に必要なもののみを表示してください。シンプルで単刀直入な言葉で要件を説明し、簡単に情報を入力できるようにしましょう。

![iPhoneに表示されたResearchKitアプリの参加資格画面のスクリーンショット。ユーザの年齢、居住地、スマートフォンのタイプを尋ねるフィールドがあります。画面の一番下には「戻る」ボタンと「送信」ボタンがあり、画面の一番上には、1つ前の画面に戻るボタンと、ヘルプボタンがあります。](https://docs-assets.developer.apple.com/published/f3b2292e1a646733fc2163dfff15121b/eligibility-screen%402x.png)

### [3.インフォームドコンセントの取得](/jp/design/human-interface-guidelines/researchkit#3-Get-informed-consent)

**ユーザが調査内容を理解した上で同意できるようにする。** ResearchKitでは、同意プロセスの簡潔さと分かりやすさを確保しつつ、法的な要件や倫理審査委員会または倫理委員会で定められた要件を同意プロセスに組み込むことができるようになっています。アプリでは必ず、該当するApp Storeガイドライン（同意要件を含む）に準拠してください。基本的に同意セクションでは、調査の仕組みを説明し、調査内容と参加者の責任を伝え、参加者の同意を得ます。

**長い同意フォームを分かりやすく細分化する。** データの収集、データの使用、得られる可能性のあるメリット、考えられるリスク、拘束時間、辞退の方法など、調査の各側面についてセクションを分け、各セクションで大まかな要点をシンプルかつ単刀直入に説明します。必要な場合は「詳しい情報」ボタンを配置し、そのセクションのさらに詳しい説明をタップで確認できるようにします。ユーザが参加に同意する前に同意フォーム全体を確認できるようにしてください。

**適宜、参加者の理解度を確認するクイズを用意する。** 対面で同意を得るときにするような質問を作成するとよいかもしれません。

![iPhoneに表示されたResearchKitアプリのクイズ画面のスクリーンショット。調査に対する理解度を確認するための多肢選択式の質問が表示されています。画面の一番下には「次へ」ボタンがあり、画面の一番上には、1つ前の画面に戻るボタンと、ヘルプボタンがあります。](https://docs-assets.developer.apple.com/published/8d1d3b066db6174020daead2a437bd7e/consent-quiz-screen%402x.png)

**参加者の同意を得たら連絡先情報を尋ねる（適宜）。** 調査への参加に同意した参加者には、確認ダイアログに続いて、署名と連絡先情報を入力するための画面が表示されます。ほとんどの研究アプリは、同意フォームの控えを参加者にPDFでメール送信しています。

![iPhoneに表示されたResearchKitアプリの同意画面のスクリーンショット。調査の重要な点について振り返ると共に、ユーザの名前を表示しています。また、調査に参加するかどうかをユーザに尋ねています。画面の一番下には「同意しない」ボタンと「同意する」ボタンがあり、画面の一番上には、1つ前の画面に戻るボタンと、ヘルプボタンがあります。](https://docs-assets.developer.apple.com/published/46b3fb7e5f95abccac05269223545a05/consent-signature-screen%402x.png)

### [4.データへのアクセス許可のリクエスト](/jp/design/human-interface-guidelines/researchkit#4-Request-permission-to-access-data)

**参加者のデバイスまたはデータへのアクセスおよび通知送信の許可を得る。** 位置情報やヘルスケアなどのデータへのアクセスがなぜ必要なのかをはっきりと説明し、調査に必須ではないデータへのアクセスはリクエストしないでください。参加者のデバイスに通知を送信する必要がある場合は、その許可もリクエストします。

![iPhoneに表示されたResearchKitアプリの同意画面のスクリーンショット。調査の重要な点について振り返っています。また、データを研究者が今後の研究でも使えるように共有するか、今回の調査に限って共有するかを選べる選択肢があります。画面の一番下には「同意する」ボタンがあり、画面の一番上には、1つ前の画面に戻るボタンと、ヘルプボタンがあります。](https://docs-assets.developer.apple.com/published/f6ba2397244ced15b0c32cfaefec4352/permissions-health-data-screen%402x.png)

## [研究の実施](/jp/design/human-interface-guidelines/researchkit#Conducting-research)

参加者からの情報を得るには、アンケートとアクティブタスクのいずれかまたは両方を使用します。参加者が各セクションを複数回操作することもあれば1回限りのこともあり、これは調査をどのように設計するかによって異なります。

**参加者の積極性を維持できるアンケートを作成する。** ResearchKitには、アンケート向けのカスタマイズ可能画面が数多く用意されており、はい/いいえ式、多肢選択式、日時選択式、スライディングスケール、自由記述式といった多種多様な回答タイプの質問を簡単に作成できるようになっています。ResearchKit画面を使ってアンケートを作成する場合、優れた体験を提供するには以下のガイドラインに従ってください:

  * 合計質問数と回答所要時間を伝える。

  * 1つの質問につき1つの画面を使う。

  * 何問中何問完了したか分かるようにする。

  * アンケート自体をできる限り短くする。長いアンケートを1回行うよりも短いアンケートを複数回実施する方が効果的。

  * 質問で追加説明が必要な場合は、質問文に標準フォントを使用し、説明テキストのフォントはやや小さくする。

  * 回答が完了したことを参加者に伝える。

![iPhoneに表示されたResearchKitアプリのアンケート画面のスクリーンショット。パーキンソン病の症状をリストから選択し、「次へ」ボタンをタップしてアンケートの次の項目に進むよう促しています。画面の一番上には「閉じる」ボタンがあります。](https://docs-assets.developer.apple.com/published/b792666c931e2f2a9bcdfbdaa1150c0f/survey-question-type1-screen%402x.png)

**アクティブタスクについて分かりやすく説明する。** アクティブタスクは、マイクに向かって話す、画面を指でタップする、歩く、記憶力テストを受けるといったアクティビティの実施を参加者に求めるものです。参加者にアクティブタスクの実施を促し、参加者がそのタスクを確実に正しく実行できるようにするには、以下のガイドラインに従ってください:

  * タスクの実行方法を、はっきりとしたシンプルな言葉で説明する。

  * タスクを実行する時間帯や実行の状況に決まりがある場合は、その要件を説明する。

  * タスクを完了したことが参加者に分かるようにする。

![iPhoneに表示されたResearchKitアプリのアクティブタスク画面のスクリーンショット。人が歩いているイラストと、「歩く」と「バランス」のアクティブタスクの実行方法を説明する指示文が表示されています。要件のリストが「開始」ボタンと共に表示されています。画面の一番上には「閉じる」ボタンがあります。](https://docs-assets.developer.apple.com/published/86e98640b260c14bba585793ea9c43ad/active-tasks-screen%402x.png)

## [個人情報の管理とモチベーションの提供](/jp/design/human-interface-guidelines/researchkit#Managing-personal-information-and-providing-encouragement)

ResearchKitには、研究アプリで使用する個人情報を参加者が管理することができるプロフィール画面があります。これに加えて、参加者にモチベーションを与え、調査の進行状況のトラッキング手段を提供するカスタム画面をデザインするのもおすすめです。どちらの画面もアプリの使用中にいつでもアクセスできるようになっているのが理想です。

**調査に関連した個人データを参加者がプロフィールで管理できるようにする。** プロフィール画面には、調査の期間中に変化があったデータ（体重や睡眠習慣など）を編集できる機能があるほか、予定されているアクティビティのリマインダーが表示されるようになっています。プロフィール画面から簡単に調査を辞退したり、同意書類やプライバシーポリシーなどの重要な情報を確認したりできるようにすることも可能です。

![iPhoneに表示されたResearchKitアプリのプロフィール画面のスクリーンショット。氏名や誕生年などの個人情報を入力するフィールドが並んでいます。各フィールドには、フィールドの値を編集するためのボタンがあります。画面の一番上には設定ボタンがあり、画面の一番下には「トラッキング」、「履歴」、「プロフィール」の各タブがあります。「プロフィール」タブがアクティブになっています。](https://docs-assets.developer.apple.com/published/9112be9b40dfaec1cc5270f94adc4645/profile-screen%402x.png)

**ダッシュボードを使って進行状況を伝え、継続のモチベーションを与える。** 適宜、ダッシュボードを使って参加者の意欲を引き出すようなフィードバックを提供しましょう。例えば、毎日の進行状況や週ごとの評価、特定のアクティビティの結果を表示したり、さらには自分の結果とほかの参加者の集約結果を比較できるようにしたりするのもよいでしょう。

![iPhoneに表示されたResearchKitアプリの履歴画面のスクリーンショット。この画面には、ユーザが2日間で実行したアクティブタスクの記録が表示されています。画面の一番下には「トラッキング」、「履歴」、「プロフィール」の各タブがあります。「履歴」タブがアクティブになっています。](https://docs-assets.developer.apple.com/published/25406660a2e86f4d4938937badc4ed62/dashboard-screen%402x.png)

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/researchkit#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/researchkit#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/researchkit#Related)

[Research & Care > ResearchKit](https://www.researchandcare.org/researchkit/)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/researchkit#Developer-documentation)

[Research & Care > Developers](https://www.researchandcare.org/developers/)

[ユーザのプライバシーの保護](/documentation/HealthKit/protecting-user-privacy) — HealthKit

[ResearchKit GitHubプロジェクト](https://github.com/ResearchKit/ResearchKit)

#### [ビデオ](/jp/design/human-interface-guidelines/researchkit#Videos)

[](https://developer.apple.com/videos/play/wwdc2020/10151)

[](https://developer.apple.com/videos/play/wwdc2021/10068)

[](https://developer.apple.com/videos/play/wwdc2019/217)

## [変更履歴](/jp/design/human-interface-guidelines/researchkit#Change-log)

日付| 変更内容  
---|---  
2023年9月12日| アートワークをアップデート。
