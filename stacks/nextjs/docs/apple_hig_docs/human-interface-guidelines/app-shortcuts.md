# アプリショートカット

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/app-shortcuts

# アプリショートカット

アプリショートカットを使用すると、システム全体でアプリの重要な機能やコンテンツにアクセスできるようになります。

![図案化されたSpotlight。トップヒットの結果としてメモアプリが表示されていて、新規メモの作成や最近開いた2つのメモについてのショートカットが表示されています。画像全体が、6色の初代Appleロゴの赤色を連想させる赤みを帯びています。](https://docs-assets.developer.apple.com/published/f5b04eaa160408ab1d03a6ed85d938c0/components-app-shortcuts-intro%402x.png)

アプリショートカットは、[Siri](/jp/design/human-interface-guidelines/siri)、Spotlight、ショートカットアプリなどの機能から開始できます。また、iPhoneやApple Watchの[アクションボタン](/jp/design/human-interface-guidelines/action-button)のようなハードウェア機能や、Apple Pencilの[スクイーズ](/jp/design/human-interface-guidelines/apple-pencil-and-scribble#Squeeze)を使って開始することもできます。

アプリショートカットはアプリの一部なので、インストールが完了するとすぐに使えるようになります。例えば、ジャーナリングアプリで新しいジャーナルエントリーを作成するためのアプリショートカットを提供する場合、アプリを初めて開く前でも利用できます。アプリの利用が開始されると、そのアプリショートカットに選択肢を反映できます。例えば、最近の連絡先と通話するために、FaceTimeの選択肢を利用できます。

![iPhoneのショートカットアプリのスクリーンショットの一部。グリッドビューにFaceTimeのアプリショートカットが表示されています。アプリショートカットは「最近の項目に発信」というラベルがついたグループに含まれており、最近のFaceTime連絡先の名前がそれぞれのタイトルになっています。](https://docs-assets.developer.apple.com/published/d65a35ae546f0799e394ba39d4ebc31d/app-shortcuts-personalized-choices%402x.png)

アプリショートカットは、[App Intents](/documentation/AppIntents)を使用してアプリ内のアクションを定義し、システムが利用できるようにします。各アプリショートカットには、1つまたは複数のアクションが含まれます。アクションは、ユーザがタスクを実行する一連の手順を表します。例えば、ホームセキュリティアプリでは、夜寝るときに照明を消して外のドアに鍵をかけるという2つの一般的なアクションを組み合わせて、1つのアプリショートカットにすることができます。1つのアプリに、最大10個のアプリショートカットを含めることができます。

注意

App Intentを使ってアプリのアクションをシステムに公開する場合は、アプリが提供するアプリショートカットに加えて、ショートカットアプリのアクションを組み合わせて独自のカスタムショートカットを作成することもできます。カスタムショートカットでは、ユーザがアクションの動作を柔軟に構成できるほか、複数のアプリ間でタスクを実行するワークフローも可能になります。追加のガイダンスは、「[ショートカットユーザガイド](https://support.apple.com/guide/shortcuts/welcome/ios)」を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/app-shortcuts#Best-practices)

**アプリで特によく使う重要なタスクのアプリショートカットを提供する。** 現在のコンテキストを離れることなく完了できる単純なタスクが最適ですが、複数のタスクを簡単に完了できる場合は、アプリを開くこともできます。

**ユーザがオプションを選べるようにして柔軟性を高める。** 妥当な場合、アプリショートカットに1つのオプション値（パラメータ）を含めることができます。例えば瞑想アプリでは、次のようにして特定のタイプの瞑想を始めるアプリショートカットを提供できます: 「[朝の, いつもの, 就寝前の]瞑想をスタート」ユーザは値のリストを見ながら選ぶわけではないので、予想しやすい、よくある値をオプションとして含めてください。デベロッパ向けのガイダンスは、[App Intentにパラメータを追加する](/documentation/AppIntents/Adding-parameters-to-an-app-intent)を参照してください。

![コーヒーアプリからドリンクを注文するショートカットの起動フレーズの図。起動フレーズには、下線が付いたドリンク名のオプション値が含まれています。これがショートカットのパラメータとして呼び出されます。](https://docs-assets.developer.apple.com/published/d7c9ef89ac442b4edd9855b698e0f207/app-intents-parameter-diagram%402x.png)

**オプションの情報が存在しないリクエストに対して確認を行う。** 例えば、タイプ（「朝の」、「いつもの」、または「就寝前の」）を指定せずに「瞑想をスタート」というようにユーザが言った場合、最後に使ったタイプや現在の時間に基づくタイプを提案することでフォローアップできます。可能性が高いオプションがある場合は、それをデフォルトとして提示し、デフォルト以外のものを選択したい場合のために、別の選択肢の短いリストを表示することを検討してください。

**音声操作は簡潔にする。** 自分で声に出して言ってみたときに複雑に感じるようだと、おそらくユーザにとっても難しすぎて、覚えたり正確に言ったりすることができないでしょう。例えば、「自然の音で[就寝前の]瞑想を始める」のようなフレーズは、瞑想のタイプとそれに付随するサウンドという2つのパラメータがあるように誤解されかねません。追加情報がどうしても必要な場合は、フレーズの発話後のステップでリクエストします。音声操作のダイアログのテキスト作成に関する追加のガイダンスについては、[Siri](/jp/design/human-interface-guidelines/siri)を参照してください。

**アプリでアプリショートカットを見つけやすくする。** ショートカットが利用できることが分かれば、頻繁に行うタスクのアプリショートカットを覚えて使ってもらえる可能性が高くなります。ユーザがアプリで一般的なアクションを実行するときに、アプリショートカットの存在を知らせるヒントをときどき表示することを検討してください。デベロッパ向けのガイダンスは、[`SiriTipUIView`](/documentation/AppIntents/SiriTipUIView)を参照してください。

### [アプリショートカットへの応答方法](/jp/design/human-interface-guidelines/app-shortcuts#Responding-to-App-Shortcuts)

ユーザがアプリショートカットを使うとき、アプリはさまざまな方法で応答できます。例えば、Siriによる読み上げや、スニペットやライブアクティビティのようなカスタムのビジュアルなどです。

  * 静的な情報や、ユーザの現在地の天気を表示する、注文を確認するといったダイアログのオプションを表示するカスタムビューには、スニペットが最適です。デベロッパ向けのガイダンスは、[`ShowsSnippetView`](/documentation/AppIntents/ShowsSnippetView)を参照してください。

  * [ライブアクティビティ](/jp/design/human-interface-guidelines/live-activities)では、ユーザが関心を持ち、時間によって変化する情報に連続的にアクセスできるので、イベントが終了するまで表示されるタイマーやカウントダウンに最適です。デベロッパ向けのガイダンスは、[`LiveActivityIntent`](/documentation/AppIntents/LiveActivityIntent)を参照してください。

![iPhoneのホーム画面のスクリーンショット。画面の上半分がカスタムスニペットで占められています。スニペットには、コーヒーショップの注文の配達を確認またはキャンセルするためのボタンに加え、注文品目と合計価格が表示されています。](https://docs-assets.developer.apple.com/published/2f1d07f07013f89e0d77db1428a00fb1/app-shortcuts-siri-dialogue%402x.png)

![iPhoneのホーム画面のスクリーンショット。画面の上4分の1がライブアクティビティで占められています。ライブアクティビティには、コーヒーショップの注文の配達予定到着日時に加え、注文の品目数と配送ドライバーに連絡するボタンが表示されています。](https://docs-assets.developer.apple.com/published/a7ac77fe3d2688809e63aff2804d73f1/app-shortcuts-live-activity%402x.png)

**音声専用デバイス向けに詳細な対話方法を提供する。** ユーザは、AirPodsやHomePodなどの音声専用デバイスで応答を受け取る可能性もあり、画面にコンテンツを表示できるとは限りません。重要な情報は、すべてアプリショートカットの対話テキストに含めるようにしてください。デベロッパ向けのガイダンスは、[`init(full:supporting:systemImageName:)`](/documentation/AppIntents/IntentDialog/init\(full:supporting:systemImageName:\))を参照してください。

## [表記等に関するガイドライン](/jp/design/human-interface-guidelines/app-shortcuts#Editorial-guidelines)

**短く覚えやすい起動フレーズと自然なバリアントを提供する。** Siriでアプリショートカットを起動する場合、ユーザはアプリショートカットのフレーズ（または定義するバリアント）を話すので、短く覚えやすいものにすることが重要です。アプリ名を含めることは必須ですが、自由に工夫してかまいません。例えばKeynoteでは、新規書類を作成するアプリショートカットのフレーズとして、「Keynoteを作成」と「新しいプレゼンテーションをKeynoteに追加」の両方を利用できます。デベロッパ向けのガイダンスは、[`AppShortcutPhrase`](/documentation/AppIntents/AppShortcutPhrase)を参照してください。

**アプリショートカットまたはショートカットアプリに言及するときは、ショートカットに引用符を付けるか _ショートカット_ アプリと表記する。**例えば、「 _このアプリは“ショートカット”と連係しているため、タップするかSiriに頼むだけで素早くタスクを実行できます。アプリショートカットをアクションボタンに配置することもできます。_ 」などとします。

**アプリショートカットやショートカットアプリではなく個々のショートカットに言及するときは引用符は不要。** 例えば、「 _ショートカットを実行するには、Siriに頼むか、ロック画面に表示された提案をタップします。_ 」などとします。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/app-shortcuts#Platform-considerations)

 _visionOS、watchOSに追加の考慮事項はありません。tvOSには対応していません。_

### [iOS/iPadOS](/jp/design/human-interface-guidelines/app-shortcuts#iOS-iPadOS)

アプリショートカットは、ユーザがアプリを検索するときにSpotlightのトップヒット領域または下のショートカット領域に表示できます。各アプリショートカットは、その機能を表すための[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)のシンボルや、ショートカットが直接リンクする項目のプレビュー画像と一緒に表示されます。

![iPhoneのSpotlightの検索結果のスクリーンショットの一部。画面上部のトップヒット領域と、その下の候補領域が表示されています。トップヒットとしてメモアプリが表示され、アプリアイコンの右側にアプリショートカットが並んで表示されています。「新規メモ」というタイトルには正方形と斜めになった鉛筆のシンボルが、「クイックメモ」というタイトルにはキャンバスに落書きのような線のシンボルが表示され、「Nature」というタイトルには最近のメモが埋め込まれたサムネール画像が表示されています。候補領域には、「not」のWeb検索へのリンクと、オートコンプリート語句の候補として「noteworthy」と「notes」が表示されています。](https://docs-assets.developer.apple.com/published/449b6c2435f42071bd185b75f4f8dce4/app-shortcuts-spotlight-search-top-hit%402x.png)

**ショートカットは重要度に基づいた順序で並べる。** 選択した順番により、Spotlightとショートカットアプリの両方のアプリショートカットの初期表示順が決まります。そのため、一番汎用的なものを一番前にするのが効果的です。ユーザがアプリショートカットを使い始めると、一番よく使われるものが優先されるようにアップデートされます。

**ライブアクティビティを開始するアプリショートカットを提供する。** ライブアクティビティを使用すると、ユーザがどのデバイスでも一目でわかる場所でイベントやタスクの進行状況をトラッキングできます。例えば、料理アプリでは、料理をオーブンから取り出すまでの残り時間を表示するライブアクティビティを提供できます。ユーザがキッチンタイマーを簡単に開始できるように、アプリでユーザがアクションボタンに配置できるアプリショートカットを提供します。ライブアクティビティについて詳しくは、[ライブアクティビティ](/jp/design/human-interface-guidelines/live-activities)を参照してください。

### [macOS](/jp/design/human-interface-guidelines/app-shortcuts#macOS)

アプリショートカットは、macOSでは利用できません。ただし、App Intentを使って作成されたアプリのアクションは利用でき、そのアクションを使ってMacのショートカットアプリでカスタムショートカットを作成することもできます。

## [リソース](/jp/design/human-interface-guidelines/app-shortcuts#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/app-shortcuts#Related)

[Siri](/jp/design/human-interface-guidelines/siri)

[Siriスタイルガイド](https://developer.apple.com/siri/style-guide/)

[ショートカットユーザガイド](https://support.apple.com/guide/shortcuts/welcome/ios)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/app-shortcuts#Developer-documentation)

[App Intents](/documentation/AppIntents)

[SiriKit](/documentation/SiriKit)

[アクションとコンテンツを見つけられるようにして広く提供する](/documentation/AppIntents/Making-actions-and-content-discoverable-and-widely-available) — App Intents

[カスタムのデータタイプをインテントに組み込む](/documentation/AppIntents/Integrating-custom-types-into-your-intents) — App Intents

#### [ビデオ](/jp/design/human-interface-guidelines/app-shortcuts#Videos)

[](https://developer.apple.com/videos/play/wwdc2025/281)

[](https://developer.apple.com/videos/play/wwdc2025/244)

[](https://developer.apple.com/videos/play/wwdc2024/10210)

## [変更履歴](/jp/design/human-interface-guidelines/app-shortcuts#Change-log)

日付| 変更内容  
---|---  
2025年1月17日| ガイダンスを簡潔にして更新。  
2023年6月05日| 新規ページ。
