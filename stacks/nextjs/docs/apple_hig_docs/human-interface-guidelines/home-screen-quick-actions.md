# ホーム画面のクイックアクション

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/home-screen-quick-actions

# ホーム画面のクイックアクション

ホーム画面のクイックアクションは、ユーザがホーム画面からアプリ固有のアクションを実行できる機能です。

![アプリアイコンから上に伸びている図案化されたメニューのアイテム。画像は6色のオリジナルAppleロゴをイメージさせる赤色になっています。](https://docs-assets.developer.apple.com/published/4563cf1129f7820f779bfd64505387e5/components-home-screen-quick-actions-intro%402x.png)

ユーザがアプリアイコンをタッチして押さえたままにすると、利用可能なクイックアクションのメニューが表示されます（3D Touchデバイスでは、アイコンを強めに押すとメニューが表示されます）。例えば「メール」のクイックアクションでは、受信トレイやVIPメールボックスを開いたり、検索を開始したり、新規メッセージを作成したりできます。ホーム画面のクイックアクションメニューから、アプリ固有のアクションだけでなく、アプリの削除やホーム画面の編集も実行できます。

ホーム画面のクイックアクション項目には、タイトル、その左か右にインターフェイスアイコン（アプリのホーム画面上の位置による）、オプションのサブタイトルが表示されます。左から右に記述する言語では、タイトルとサブタイトルは常に左揃えになります。アプリで新しい情報が利用可能になるのに応じて、クイックアクションを動的にアップデートすることもできます。例えば「メッセージ」には、最新の会話を開くクイックアクションがあります。

## [ベストプラクティス](/jp/design/human-interface-guidelines/home-screen-quick-actions#Best-practices)

**魅力ある価値の高いタスクを実行するクイックアクションを作成する。** 例えば「マップ」には、現在地の周辺を検索したり、自宅までの経路を表示したりするクイックアクションがあります。これを実行するために先にマップアプリを開く必要はありません。多くのユーザは、どのアプリでも最低1つの便利なクイックアクションが用意されていることを期待しています。全部で4つまで設定できます。

**予測不能な変更をクイックアクションに加えない。** 動的クイックアクションは、アクションを常に関連性の高いものにできる優れた方法です。例えば、現在地やアプリでの最新のアクティビティ、時刻、設定の変更に基づいてクイックアクションをアップデートすると便利な場合があります。アクションの変更はユーザが予測できるものにしてください。

**各クイックアクションに、それを実行するとどうなるかがすぐに分かる簡潔なタイトルを付ける。** 例えば、「自宅への経路」、「新規連絡先を作成」、「新規メッセージ」などのタイトルを付けると、そのアクションを選択するとどうなるかが分かりやすくなります。もっと詳しい情報が必要な場合は、サブタイトルも提供してください。「メール」では、受信トレイやVIPフォルダに未開封メッセージがあるかどうかを示すサブタイトルを使用しています。タイトルやサブタイトルにアプリ名や無関係な情報を含めないでください。テキストは切り捨てが発生しないように短くし、ローカリゼーションも考慮に入れる必要があります。

**クイックアクションごとに使い慣れたインターフェイスアイコンを付ける。** アクションを表す[SF Symbols](/jp/design/human-interface-guidelines/sf-symbols)の使用を優先してください。一般的なアクションを表すアイコンのリストは、[標準のアイコン](/jp/design/human-interface-guidelines/icons#Standard-icons)を参照してください。追加のガイダンスは[メニュー](/jp/design/human-interface-guidelines/menus)を参照してください。

独自のインターフェイスアイコンをデザインする場合は、[iOSとiPadOSのAppleのデザインリソース](https://developer.apple.com/design/resources/#ios-apps)に収録されているクイックアクションアイコンテンプレートを使います。

**絵文字をシンボルやインターフェイスアイコンの代わりに使わない。** 絵文字はフルカラーですが、クイックアクションシンボルはモノクロで、ダークモードではコントラストを維持するために見た目が変わります。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/home-screen-quick-actions#Platform-considerations)

 _iOS、iPadOSに追加の考慮事項はありません。macOS、tvOS、visionOS、watchOSには対応していません。_

## [リソース](/jp/design/human-interface-guidelines/home-screen-quick-actions#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/home-screen-quick-actions#Related)

[メニュー](/jp/design/human-interface-guidelines/menus)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/home-screen-quick-actions#Developer-documentation)

[ホーム画面にクイックアクションを追加する](/documentation/UIKit/add-home-screen-quick-actions) — UIKit
