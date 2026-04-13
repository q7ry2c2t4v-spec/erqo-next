# コントロール

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/controls

# コントロール

iOSおよびiPadOSのコントロールでは、コントロールセンター、ロック画面、アクションボタンからアプリの機能に素早くアクセスすることができます。

![コントロールセンターにある機内モードトグル、Wi-Fiトグル、AirPlayボタンなどのコントロールが写ったスクリーンショットの一部。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/0cea7197d96a9a3bfadc6aed2942b027/components-controls-intro%402x.png)

コントロールとは、システムのほかの領域からアプリの機能に素早くアクセスできるボタンやトグルのことです。コントロールボタンでは、アクションを実行したり、アプリの特定の領域にリンクしたり、[ロックされたデバイスでのカメラ体験](/jp/design/human-interface-guidelines/controls#Camera-experiences-on-a-locked-device)を起動したりできます。コントロールトグルでは、オン/オフなどの2つの状態を切り替えることができます。

コントロールセンターの空の領域を長押ししたり、ロック画面をカスタマイズしたり、設定アプリでアクションボタンを設定したりすることで、それぞれの場所にコントロールを追加することができます。

## [構造](/jp/design/human-interface-guidelines/controls#Anatomy)

コントロールにはシンボル画像とタイトルが含まれ、さらに値を含めることもできます。シンボルはコントロールの機能を視覚的に表すもので、[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)のシンボルまたはカスタムシンボルを使用することができます。タイトルはコントロールが何に関連するものかを表し、値はコントロールの状態を表します。例えば、タイトルには部屋の照明の名前を、値にはその照明のオン/オフを表示することができます。

![コントロールトグルにおけるシンボル画像、タイトル、値の配置を示す図。](https://docs-assets.developer.apple.com/published/c9bdd36ed20a8c4cdcc63ab33a355be7/control-medium-anatomy%402x.png)

コントロールでの情報の表示方法は、コントロールの場所によって異なります:

  * コントロールセンターのコントロールには、シンボルに加えて、大きなサイズのタイトルと値が表示されます。

  * ロック画面のコントロールには、シンボルが表示されます。

  * アクションボタンに割り当てられたコントロールのあるiPhoneデバイスでは、コントロールを長押しすると、Dynamic Islandにコントロールのシンボルが表示され、（値がある場合は）値も表示されます。

![iPhoneのコントロールセンターのスクリーンショットの一部。ベルのシンボルに斜線が引かれて赤くなっていて、消音モードのコントロールがアクティブであることが強調されています。](https://docs-assets.developer.apple.com/published/b05d2923dc01d6719a8c662bc3be0352/control-control-center%402x.png)

コントロールセンターのコントロールトグル

![iPhoneのロック画面下部のスクリーンショットの一部。ベルのシンボルに斜線が引かれて赤くなっていて、右側で消音モードのコントロールがアクティブであることが強調されています。](https://docs-assets.developer.apple.com/published/912ae3e318cf61d7146965079dc682cb/control-lock-screen%402x.png)

ロック画面のコントロールトグル

![iPhoneのホーム画面上部のDynamic Islandが表示されたスクリーンショットの一部。主要領域にある斜線が引かれて赤くなったベルのシンボルと、後続領域にある「消音」という赤いテキストによって、消音モードのコントロールがアクティブであることが示されています。](https://docs-assets.developer.apple.com/published/12ab1d6fa4525acf5409575d04a8ed4b/control-dynamic-island%402x.png)

アクションボタンから実行される Dynamic Islandのコントロールトグル

## [ベストプラクティス](/jp/design/human-interface-guidelines/controls#Best-practices)

**アプリを起動せずに利用できると便利なアクションに対してコントロールを提供する。** 例えば、コントロールからライブアクティビティを起動できると、アプリに移動して最新情報を把握しなくても、簡単かつシームレスに進捗を知ることができます。ガイダンスは[ライブアクティビティ](/jp/design/human-interface-guidelines/live-activities)を参照してください。

**コントロールが操作されたとき、アクションが完了したとき、またはプッシュ通知によってリモートでコントロールをアップデートする。** コントロールのコンテンツをアップデートして、状態を正確に反映させ、アクションが進行中であるかどうかを示すようにします。

**コントロールの動作を表す分かりやすいシンボルを選択する。** コントロールが追加される場所によっては、タイトルと値は表示されない場合があるため、シンボルによってコントロールのアクションの情報が十分に伝わる必要があります。コントロールトグルでは、オン/オフ両方の状態のシンボルを提供してください。例えば、ガレージドアを開閉するコントロールを表すには、SF Symbolsの`door.garage.open`と`door.garage.closed`を使用します。ガイダンスは、[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)を参照してください。

**シンボルのアニメーションは状態の変化を強調するために使う。** コントロールトグルでは、オン/オフ両方の状態の間のトランジションをアニメートします。継続時間があるアクションのコントロールボタンでは、アクションの実行中は無期限にアニメートし、アクションが完了したらアニメートを停止します。デベロッパ向けのガイダンスは、[Symbols](/documentation/Symbols)および[`SymbolEffect`](/documentation/Symbols/SymbolEffect)を参照してください。

**アプリのブランドに合う色合いを選択する。** この色合いは、コントロールトグルのシンボルがオン状態のとき、そのシンボルに適用されます。アクションボタンからコントロールのアクションが実行されると、Dynamic Islandに表示される値とシンボルにもこの色合いが使用されます。ガイダンスは、[ブランディング](/jp/design/human-interface-guidelines/branding)を参照してください。

![色の付いていない電球のシンボルが表示された、アクティブでないコントロールトグル。](https://docs-assets.developer.apple.com/published/858a6c878e81223350b2c6175e7edc8d/control-lightbulb-not-tinted%402x.png)色の付いていないオフ状態のコントロールトグル

![黄色い電球のシンボルが表示された、アクティブなコントロールトグル。](https://docs-assets.developer.apple.com/published/6beab4a3187d3a10493645eaf5447811/control-lightbulb-tinted%402x.png)色の付いたオン状態のコントロールトグル

**アクションの実行に必要な追加情報をユーザが提供できるようにする。** 目的のアクションを実行するために、ユーザによるコントロールの設定が必要な場合があります（オン/オフを切り替える特定の照明を家の中から選択する場合など）。設定が必要なコントロールでは、最初にコントロールを追加したときにこの手順を完了するようにユーザを促してください。コントロールはいつでも再設定することができます。デベロッパ向けのガイダンスは、[`promptsForUserConfiguration()`](/documentation/SwiftUI/ControlWidgetConfiguration/promptsForUserConfiguration\(\))を参照してください。

![ユーザが選択した値にオプションを設定できるコントロールを表した図。](https://docs-assets.developer.apple.com/published/31431441dfd67296fc178a3d88b1a8b4/control-configuration-options%402x.png)

**アクションボタンにはヒントテキストを用意する。** ユーザがアクションボタンを押すと、長押しした場合の動作を説明するヒントテキストが表示されます。アクションボタンを長押しすると、そこに設定されたアクションが実行されます。ヒントテキストには動詞を使用します。デベロッパ向けのガイダンスは、[`controlWidgetActionHint(_:)`](/documentation/SwiftUI/View/controlWidgetActionHint\(_:\)-5yoyh)を参照してください。

![アクションボタンのヒントテキストが表示されたiPhoneのホーム画面のスクリーンショットの一部。ヒントテキストには「長押しで消音」と書かれています。](https://docs-assets.developer.apple.com/published/633606183352f1eab9a57f9b4e37bfb5/controls-action-button-coaching-text-on%402x.png)

![アクションボタンのヒントテキストが表示されたiPhoneのホーム画面のスクリーンショットの一部。ヒントテキストには「長押しで着信音」と書かれています。](https://docs-assets.developer.apple.com/published/e0432b259a908487a50da6c62879cc9e/controls-action-button-coaching-text-off%402x.png)

**コントロールのタイトルや値が変化する場合はプレースホルダを含める。** タイトルと値が状況に応じて変化する場合、プレースホルダの情報によってコントロールの動作が伝わります。この情報は、ユーザがコントロールセンターやロック画面でコントロールのギャラリーを開いてコントロールを選択したとき、またはそのコントロールをアクションボタンに割り当てる前に表示されます。

**デバイスがロックされているときは機密情報を隠す。** デバイスがロックされているときは、個人情報やセキュリティ関連の情報を隠すために、タイトルと値を墨消しすることを検討してください。シンボルの状態も墨消しする必要があるかどうかを指定します。指定された場合は、タイトルと値が墨消しされ、シンボルはオフ状態で表示されます。

![中サイズのコントロールトグルに、電球のシンボル、タイトル、値テキストが表示されています。](https://docs-assets.developer.apple.com/published/1c88de255b68d29988d893ba7680cf90/control-regular-text%402x.png)すべての情報が表示されているコントロールトグル

![中サイズのコントロールトグルに、墨消しされたテキストが表示されています。](https://docs-assets.developer.apple.com/published/60fdc68e4ffd056e2ced9b7c49ed6730/control-redacted-text%402x.png)ロックされたデバイス上の情報が隠されたコントロールトグル

**セキュリティに影響するアクションには認証を要求する。** 例えば、家のドアをロック/ロック解除するコントロールや車を始動するコントロールにアクセスするには、デバイスをロック解除する必要があるようにします。デベロッパ向けのガイダンスは、[`IntentAuthenticationPolicy`](/documentation/AppIntents/IntentAuthenticationPolicy)を参照してください。

## [ロックされたデバイスでのカメラ体験](/jp/design/human-interface-guidelines/controls#Camera-experiences-on-a-locked-device)

アプリがカメラ撮影に対応している場合、iOS 18以降では、デバイスがロックされているときにアプリのカメラ体験を直接起動するコントロールを作成することができます。撮影以外の操作をするには、認証してデバイスをロック解除し、アプリで操作を完了する必要があります。デベロッパ向けのガイダンスは、[LockedCameraCapture](/documentation/LockedCameraCapture)を参照してください。

**アプリとカメラ体験では同じカメラUIを使用する。** UIを共有することで、ユーザがアプリに慣れていることが活かされます。同じUIを使用することで、コンテンツを撮影したユーザがボタンをタップして追加の操作を実行したとき（SNSへの投稿や写真の編集など）に、シームレスにアプリに移行することができます。

**コントロール追加のための指示を提供する。** このカメラ体験を起動するコントロールを追加する方法がユーザに分かるようにしてください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/controls#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。macOS、watchOS、tvOS、visionOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/controls#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/controls#Related)

[ウィジェット](/jp/design/human-interface-guidelines/widgets)

[アクションボタン](/jp/design/human-interface-guidelines/action-button)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/controls#Developer-documentation)

[LockedCameraCapture](/documentation/LockedCameraCapture)

[WidgetKit](/documentation/WidgetKit)

## [変更履歴](/jp/design/human-interface-guidelines/controls#Change-log)

日付| 変更内容  
---|---  
2024年6月10日| 新規ページ。
