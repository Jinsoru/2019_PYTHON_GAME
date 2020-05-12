import cx_Freeze

executables = [cx_Freeze.Executable("takoyaki.py")]

cx_Freeze.setup(
    name="TypringGame",
    # bdist_msi 
    options={"build_exe": {"packages":["pygame",],
                           "includes":["threading","time","random"],
                           "include_files":["images/angry0.png","images/angry1.png","images/angry2.png",
                                            "images/angry3.png","images/angry4.png","images/angry5.png",
                                            "images/angryOverBg.png","images/angryScreen.png", "images/back.png",
                                            "images/cooker.png", "images/end_check.png",
                                            "images/gamenotice.png", "images/goalScreen.png", "angryGame.py",
                                            "NanumPenScript-Regular.ttf", "timerGame.py", "goalGame.py",
                                            "images/icon.png","images/introBg.png","images/kettle.png",
                                            "images/mode1.png","images/mode1_checked.png","images/mode2.png",
                                            "images/mode2_checked.png","images/mode3.png","images/mode3_checked.png",
                                            "images/modeBg.png","images/mold.png","images/order1.png",
                                            "images/order2.png","images/order3.png","images/paused.png",
                                            "images/person1.png","images/person2.png","images/person3.png",
                                            "images/person4.png",
                                            "images/person5.png","images/person6.png","images/storeBg.png",
                                            "images/tako.png","images/takoyaki1.png","images/takoyaki2.png",
                                            "images/takoyaki3.png","images/takoyaki4.png","images/timeOverBg.png",
                                            "images/timerScreen.png","sound/bgm.wav","sound/click.wav",
                                            "sound/failEnd.wav","sound/key.wav","sound/no.wav",
                                            "sound/ok.wav","sound/successEnd.wav"]}},
    executables = executables

    )