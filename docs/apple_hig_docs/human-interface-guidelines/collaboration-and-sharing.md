# 共同作業と共有

> Source: https://developer.apple.com/jp/design/human-interface-guidelines/collaboration-and-sharing

# 共同作業と共有

共同作業および共有においては、シンプルさと応答性の良さこそが優れたユーザ体験となります。これによってユーザは、ほかのユーザと効果的に意思疎通しながら、コンテンツに集中できます。

![人にチェックマークが重なっているスケッチ。効果的な共同作業を示しています。画像では長方形と円形のグリッド線が重なっており、6色のオリジナルAppleロゴをイメージさせるオレンジ色になっています。](https://docs-assets.developer.apple.com/published/88653e2313edd719cb9029bac9e72cab/patterns-collaboration-and-sharing-intro%402x.png)

システムのインターフェイスやメッセージアプリは、共同作業や共有を一貫した方法で快適に行うのに役立ちます。例えば、「メッセージ」の会話の中に書類をドロップしたり、慣れ親しんだ共有シートで相手を選択したりするだけで、コンテンツの共有や共同作業が実現します。

いったん共同作業が始まったら、アプリの「共同作業」ボタンを使って、ほかのユーザとやり取りしたり、カスタムアクションを実行したり、詳細情報を管理したりできます。さらにユーザは、共同作業者がそのユーザの名前に言及したり、コンテンツに変更を加えたり、参加したり抜けたりしたときに「メッセージ」の通知を受け取れます。

デベロッパは、共同作業や共有をCloudKit、iCloud Drive、カスタムソリューションのいずれで実装しているかを問わず、「メッセージ」の統合、およびシステムが提供する共有インターフェイスを利用できます。カスタムの共同作業インフラストラクチャを使用している場合、これらの機能を利用するには、アプリがユニバーサルリンクに対応している必要があります（デベロッパ向けのガイダンスは、[アプリでユニバーサルリンクに対応する](/documentation/Xcode/supporting-universal-links-in-your-app)を参照してください）。

visionOSでは、ドキュメントの共有と共同作業に加えて、SharePlayによってイマーシブ感のある共有体験を実現できます。ガイダンスは[SharePlay](/jp/design/human-interface-guidelines/shareplay)を参照してください。

## [ベストプラクティス](/jp/design/human-interface-guidelines/collaboration-and-sharing#Best-practices)

**共有や共同作業を始めやすいように、共有ボタンをツールバーなどの使いやすい場所に配置する。** iOS 16では、システムが提供する共有シートでファイルの共有方法を選択したり、新規共同作業のアクセス権限を設定したりできます。iPadOS 16とmacOS 13では、これと類似の見た目と機能を持つポップオーバーを使用できます。SwiftUIアプリでは、選択時にシステム定義の共有シートが開く共有リンクを提示して、共有に対応することもできます。デベロッパ向けのガイダンスは、[`ShareLink`](/documentation/SwiftUI/ShareLink)を参照してください。

![iPhoneの「メモ」の書類の図。書類のツールバーでは、その他ボタンの横にある「共有」ボタンが目立つようになっています。](https://docs-assets.developer.apple.com/published/28889933af3fb0d4b3d9293b69119d64/collaboration-share-button%402x.png)

**必要に応じて共有シートまたは共有ポップオーバーをカスタマイズし、アプリが対応しているファイル共有方法を選べるようにする。** CloudKitを使用する場合、ファイルの「コピーを送信」機能を有効にするには、対象のファイルと共同作業オブジェクトの両方を共有シートにセットします。共有シートには複数項目への対応が組み込まれているので、自動的にファイルが検出され、「コピーを送信」機能が使用可能になります。iCloud Driveの場合、共同作業オブジェクトはデフォルトで「コピーを送信」機能に対応します。カスタム共同作業の場合、共有シートで「コピーを送信」機能に対応するには、ファイル（またはその内容を標準テキストに置き換えたもの）を共同作業オブジェクトに含めます。

**対応している共有権限を要約した簡潔な文言を記述する。** 例えば、「参加依頼された人のみ変更できます」とか「誰でも変更できます」のような表現が考えられます。この権限の要約は、ユーザが共同作業の定義に使う共有オプションが表示されるボタン内で使用されます。

![iPhoneの共有シートが開いている「メモ」の書類の図。選択された書類の編集権限を参加依頼された人に限定する共同作業オプションが設定されています。](https://docs-assets.developer.apple.com/published/d8e15fca8c2465cc360aed7643af38e6/collaboration-sharing-permission-invited%402x.png)

![iPhoneの共有シートが開いている「メモ」の書類の図。選択された書類をすべての人が変更できるようにする共同作業オプションが設定されています。](https://docs-assets.developer.apple.com/published/d68c1a4b6a49570a39d79c9ce3b8bd64/collaboration-sharing-permission-everyone%402x.png)

**シンプルな共有オプションを提供して共同作業の設定を簡素化する。** ユーザが権限の要約ボタンを選択すると表示されるビューをカスタマイズして、共同作業の機能が分かりやすく伝わるオプションを提示してください。例えば、誰がコンテンツにアクセスできるか、そのアクセス権は編集か読み取りのみか、共同作業者が新しい参加者を追加できるかをユーザが指定できるオプションを提示すると効果的です。カスタムのオプションはできるだけ少なくし、ユーザが一目で意味を把握できるようにグループ分けしてください。

**共同作業が開始したらすぐに「共同作業」ボタンを目立つように表示する。** ユーザはシステムが提供する「共同作業」ボタンを見て、そのコンテンツが共有されていることを意識し、誰が共有しているかに注目します。通常、「共同作業」ボタンはユーザが共有シートまたは共有ポップオーバーを操作すると表示されるので、共有ボタンの隣に配置すると効果的です。

![iPhoneで書類を開いている「メモ」の図。書類のツールバーでは、「共有」ボタンの横にある「共同作業」ボタンが目立つようになっています。](https://docs-assets.developer.apple.com/published/a5ba4d7f433f8cdf9258215d70e034a5/collaboration-status-active-collaboration-button%402x.png)

**共同作業ポップオーバーでのカスタムアクションは必要な場合にのみ提供する。** アプリで「共同作業」ボタンを選択すると、3つのセクションから成るポップオーバーが表示されます。上のセクションには共同作業者のリストと、「メッセージ」またはFaceTimeが開く通信ボタンがあります。真ん中のセクションにはカスタム項目が表示されます。下のセクションにはユーザが共有ファイルの管理に使うボタンが表示されます。情報が多すぎるとユーザに圧迫感を与えかねません。ユーザがアプリを使った共同作業中に必要とする、最も重要な項目だけを提示することがきわめて重要です。例えば「メモ」は、最新の更新情報をまとめて表示し、更新情報の詳細を入手したり、もっと多くのアクティビティを表示したりするためのボタンを提供しています。

![iPhoneの「メモ」の書類の図。書類のツールバーにある「共同作業」ボタンからメニューが開かれ、そこに最新のアップデート情報とアクティビティを表示するボタンがあります。](https://docs-assets.developer.apple.com/published/c24d6fa3efd03d577315c0fe50ac2a56/collaboration-custom-popover-notes%402x.png)

**適宜モーダルビューの共同作業管理ボタンのタイトルをカスタマイズする。** ユーザはこのボタンを選択して、設定を変更したり、共同作業者を追加または削除したりできる共同作業-管理ビューを開きます。ボタンのタイトルはデフォルトでは「共有ファイルを管理」です。CloudKit共有を使う場合は、システムから管理ビューが提供されます。それ以外の場合はビューを自分で作成してください。

**共同作業のイベント通知を「メッセージ」に投稿することを検討する。** コンテンツや共同作業メンバーの変更、参加者への言及など、起きたイベントのタイプを選択し、ユーザがアプリの関連するビューを開けるようにユニバーサルリンクを含めてください。デベロッパ向けのガイダンスは、[`SWHighlightEvent`](/documentation/SharedWithYou/SWHighlightEvent)を参照してください。

## [プラットフォームの考慮事項](/jp/design/human-interface-guidelines/collaboration-and-sharing#Platform-considerations)

 _iOS、iPadOS、macOSに追加の考慮事項はありません。tvOSでは利用できません。_

### [visionOS](/jp/design/human-interface-guidelines/collaboration-and-sharing#visionOS)

共有スペースで実行中のアプリの画面共有にデフォルトで対応しており、現在のウインドウをほかの共同作業者にストリーミングすることができます。共有中に誰かがアプリをフルスペースに移行した場合は、アプリが共有スペースに戻るまで、ほかの共同作業者へのストリーミングが自動的に一時停止します。ガイダンスは[イマーシブ体験](/jp/design/human-interface-guidelines/immersive-experiences)を参照してください。

### [watchOS](/jp/design/human-interface-guidelines/collaboration-and-sharing#watchOS)

watchOSで動作するSwiftUIアプリでは、システムが提供する共有シートを[`ShareLink`](/documentation/SwiftUI/ShareLink)を使って提示してください。

## [リソース](/jp/design/human-interface-guidelines/collaboration-and-sharing#Resources)

#### [関連情報](/jp/design/human-interface-guidelines/collaboration-and-sharing#Related)

[アクティビティビュー](/jp/design/human-interface-guidelines/activity-views)

#### [デベロッパ向けドキュメント](/jp/design/human-interface-guidelines/collaboration-and-sharing#Developer-documentation)

[Shared with You](/documentation/SharedWithYou)

[`ShareLink`](/documentation/SwiftUI/ShareLink) — SwiftUI

#### [ビデオ](/jp/design/human-interface-guidelines/collaboration-and-sharing#Videos)

[](https://developer.apple.com/videos/play/wwdc2022/10015)

[](https://developer.apple.com/videos/play/wwdc2022/10095)

[](https://developer.apple.com/videos/play/wwdc2022/10093)

## [変更履歴](/jp/design/human-interface-guidelines/collaboration-and-sharing#Change-log)

日付| 変更内容  
---|---  
2023年12月05日| ボタンの配置とさまざまな種類の共同作業権限を示すアートワークを追加。  
2023年6月21日| visionOSのガイダンスを追加するために更新。  
2022年9月14日| 新規ページ。
